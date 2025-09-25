from flask import Flask, request, jsonify
from flask_cors import CORS
from mistralai import Mistral

import pandas as pd
import numpy as np
import faiss
import os

from dotenv import load_dotenv

from src.rag.mistral_rag import MistralRag
from src.scrapper.wikipedia_scrapper import fetch_page, extract_text

load_dotenv()

app = Flask(__name__)
CORS(app)  # Allows all origins by default

# Initialise index in memory

api_key = os.getenv('MISTRAL_API_KEY')
client = Mistral(api_key=api_key)

index = None
TEXT_DF = None


def get_text_embedding(input):
    embeddings_batch_response = client.embeddings.create(
        model="mistral-embed",
        inputs=input
    )
    return embeddings_batch_response.data[0].embedding


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/set_wikipedia_url", methods=['POST'])
def set_wikipedia_url():
    data = request.json  # parse JSON payload
    wikipedia_url = data.get('wikipedia_url')  # get the 'query' field
    if not wikipedia_url:
        return jsonify({'error': 'No wikipedia url provided'}), 400
    html = fetch_page(wikipedia_url)
    text = extract_text(html)
    client = Mistral(api_key=api_key)
    mistral_rag = MistralRag(client)
    text_embeddings, chunks = mistral_rag.get_text_embeddings(text)
    embeddings_df = pd.DataFrame(text_embeddings)
    df = pd.DataFrame({
        "text_chunk": chunks
    })
    output_df = pd.concat([df, embeddings_df], axis=1)
    global TEXT_DF
    TEXT_DF = output_df[['text_chunk']]
    embeddings_df = output_df.drop(['text_chunk'], axis=1)
    text_embeddings = np.array(embeddings_df)
    d = text_embeddings.shape[1]
    global index
    index = faiss.IndexFlatL2(d)
    index.add(text_embeddings)
    return {'status': 'Succeeded'}


@app.route('/query', methods=['POST'])
def receive_query():
    data = request.json  # parse JSON payload
    query_sentence = data.get('query')  # get the 'query' field
    if not query_sentence:
        return jsonify({'error': 'No query sentence provided'}), 400
    # You can process the query_sentence here
    question_embeddings = np.array([get_text_embedding(query_sentence)])

    global index
    D, I = index.search(question_embeddings, k=5)  # distance, index
    global TEXT_DF
    chunks = TEXT_DF['text_chunk']
    retrieved_chunks_indices = [i for i in I.tolist()[0] if i != -1]
    retrieved_chunks = [chunks[i] for i in retrieved_chunks_indices]

    prompt = f"""
    Context information is below.
    ---------------------
    {retrieved_chunks}
    ---------------------
    Given the context information and not prior knowledge, answer the query.
    Query: {query_sentence}
    Answer:
    """

    def run_mistral(user_message, model="mistral-large-latest"):
        messages = [
            {
                "role": "user", "content": user_message
            }
        ]
        chat_response = client.chat.complete(
            model=model,
            messages=messages
        )
        return (chat_response.choices[0].message.content)

    answer_text = run_mistral(prompt)
    return {'answer': answer_text}


if __name__ == "__main__":
    app.run()

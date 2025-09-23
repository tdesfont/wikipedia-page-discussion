from unittest import TestCase
from mistralai import Mistral
from dotenv import load_dotenv

import os
import pandas as pd

from src.rag.mistral_rag import MistralRag

load_dotenv()


class TestMistralRag(TestCase):

    def test_mistral_rag_embeddings(self):
        with open('wikipedia_football.txt', 'r') as file:
            text = file.read()
        api_key = os.getenv('MISTRAL_API_KEY')
        client = Mistral(api_key=api_key)
        mistral_rag = MistralRag(client)
        text_embeddings, chunks = mistral_rag.get_text_embeddings(text)
        embeddings_df = pd.DataFrame(text_embeddings)
        df = pd.DataFrame({
            "text_chunk": chunks
        })
        output_df = pd.concat([df, embeddings_df], axis=1)
        output_df.to_csv("rag_embeddings.csv", index=False)

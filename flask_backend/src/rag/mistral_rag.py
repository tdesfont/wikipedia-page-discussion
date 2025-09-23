from mistralai import Mistral
import requests
import numpy as np
import faiss
import os
import tqdm
import time
import pandas as pd

api_key = "Hello"


class MistralRag:

    def __init__(self, client):
        self.client = client

    def split_in_chunks(self, text):
        chunks = []
        chunk_size = 2048
        for i in range(0, len(text), chunk_size):
            chunks.append(text[i:i + chunk_size])
        return chunks

    def process_chunks(self, chunks):
        text_embeddings = []
        for chunk in tqdm.tqdm(chunks):
            time.sleep(0.1)
            text_embeddings.append(self.get_text_embedding(chunk))
        text_embeddings = np.array(text_embeddings)
        return text_embeddings

    def get_text_embedding(self, text_chunk):
        embeddings_batch_response = self.client.embeddings.create(
            model="mistral-embed",
            inputs=text_chunk
        )
        return embeddings_batch_response.data[0].embedding

    def get_text_embeddings(self, full_text):
        chunks = self.split_in_chunks(full_text)
        text_embeddings = self.process_chunks(chunks)
        return text_embeddings, chunks



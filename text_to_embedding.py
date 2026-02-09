import os
import requests
import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity as cs
import joblib

# Creating a function for embedding using  bge-m3 embedding model.

def create_embeddings(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })
    return r.json()["embeddings"]


# Just for checking
# print(create_embeddings(["Hello, I'm Ujjwal Raj", "This is not a parameter."]))

json_files = os.listdir("newjsons")

chunk_dicts = []
chunk_id = 0

for file in json_files:
    with open(f"newjsons/{file}") as f:
        data = json.load(f)

    print(f"Creating embedings for {file}")
    embeddings = create_embeddings([c["text"] for c in data["chunks"]]) # making a list of texts from all chunks and passing to embedding function

    for i, chunk in enumerate(data["chunks"]):
        chunk["chunk_id"] = chunk_id # adding chunk id to each chunks
        chunk["embedding"] = embeddings[i] # adding embedding of each chunk
        chunk_id += 1
        chunk_dicts.append(chunk)

# print(chunk_dicts)

df = pd.DataFrame.from_records(chunk_dicts)
# print(df.head())
# print(df.tail())

# saving the data frame using joblib
file_name = "embeddings_df.joblib"
joblib.dump(df, file_name)
print(f"DataFrame saved successfully with embeddings at {file_name} !!")

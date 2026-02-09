import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity as cs
import joblib
import requests
from google import genai
from config import GEMINI_API_KEY
import time


df = joblib.load("embeddings_df.joblib")

def create_embeddings(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })
    return r.json()["embeddings"]

# Taking response from the local LLM

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.1",
        "prompt": prompt,
        "stream": False
    })
    return r.json()['response']
# Taking response with Gemini API

def inference_gemini(prompt):

    client = genai.Client(api_key= GEMINI_API_KEY)
    print("Thinking...")
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= prompt,
    )

    return response.text




#embedding the user query
def final_response(query):
    query_embedding = create_embeddings(query)[0]

    # print(query_embedding)


    # Find consine similarity of query embeddings with chunk's embeddings
    # print(df['embedding'].values)
    # print(type(df['embedding']))
    # print(type(df['embedding'].values))
    # print(np.vstack(df['embedding']))
    # print(type(np.vstack(df['embedding'])))

    similarities = cs(np.vstack(df['embedding']), [query_embedding]).flatten()

    # print(similarities)

    top_num = 10
    top_idx = np.argsort(similarities)[::-1][:top_num] # Top  similarities indexies
    # print(top_idx)


    # retriving top similarity rows from data frame

    top_df = df.loc[top_idx]

    prompt = f'''assume your self as a guide of course (Explora) which I'm teaching Python of MIT OpenCourseWare. Here are the video subtitle chunks containing video title, start timestamp, end timestamp and the text at the time : 
    {top_df[["title", "text", "start", "end"]].to_json(orient = "records")}
    -------------------------------------------
    "{query}"
    user asked this question related to the video chunks, you have to answer in humanized way (do not mention the above format, its just for you) where and how much content is taught in which video (in which video and what timestamp) and guide the user to go to that particular video. If user asks really unrelated question or questions,forget the given data(chunks) and  answer only if the question is general conversational other wise tell him that you can only answer questions related to the course, as It is a particular course topics.
    '''


    with open("prompt.txt", "w") as f:
        f.write(prompt)

    # for index, items in top_df.iterrows():
    #     print(index, items["title"], items["text"], items["start"], items["end"])

    # print(top_df[["text", "start", "end"]])

    # response with local LLM
    # response = inference(prompt)

    # response with Gemini API
    response = inference_gemini(prompt)

    return response


if __name__ == "__main__":
    
# Taking query from the user
    isExit = False
    while not isExit:
        query = input("Ask a question : ")

        response = final_response(query)

        for chunk in response:
            print(chunk, end="")
            time.sleep(0.2)
        print()


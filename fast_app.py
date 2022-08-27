"""
pip install fastpi
pip install uvicorn


Docs:

    GET : getting resource from server
    POST: creating a resource on the server

Modules

- Native
- third party libraries

spacy 3.4.5
    - requests 11.x.x

spacy 3.4.5
requests 9.x.x

"""

from ml import nlp
from fastapi import FastAPI


app = FastAPI()

import json


@app.get("/")
def read_msg():
    return {"message": "hello world"}


@app.get("/article/{article_id}")
def analyze_article(article_id: int, query: str = None):
    """ analyzes article and produces entities from article """

    if query:
        doc = nlp(query)
        ents = []
        for ent in doc.ents:
            ents.append({"text": ent.text, "label": ent.label_})

    return {
        "article_id": article_id,
        "query": query,
        "entities": ents}




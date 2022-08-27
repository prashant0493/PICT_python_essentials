"""

List of commands to install requirements.
    - pip install fastpi
    - pip install uvicorn


HTTP methods:

    GET : getting resource from server
    POST: creating a resource on the server

Modules

- Native ( modules that get installed along Python installation )
- third party libraries ( modules that are explicitly installed using package manager `pip` )


Why we should create virtual environment?
    - To isolate packages along with their specific versions
    - To manage package dependencies.
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




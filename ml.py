"""
virtualenv venv
source venv/bin/activate
pip install spacy
python -m spacy download en_core_web_sm

"""

import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Apple buys UK based startup for $1 Billion")

for ent in doc.ents:
    print(ent.text, ent.label_)

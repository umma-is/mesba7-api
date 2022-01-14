from flask import Flask
import arrand.arrandom
from flask_cors import CORS
from flask import request
import re


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'ok'

@app.route('/random')
def random():
    max_length = 4
    vocalized = False

    if request.args:
        args = request.args

        if "sentences_count" in args:
            max_length = int(args["sentences_count"])

        if "vocalized" in args:
            v = False
            if args["vocalized"].lower() == "true":
                v = True
            vocalized = v
    
    t = []
    needed_count = max_length
    while needed_count > 0:
        res = arrand.arrandom.rand_sentences(needed_count)
        res = clean_results(res, "")
        t.extend(res)
        needed_count -= len(res)

    return {
        "result": t
    }

@app.route('/sample')
def sample():
    max_length = 4
    category = "text"
    vocalized = False

    if request.args:
        args = request.args

        if "sentences_count" in args:
            max_length = int(args["sentences_count"])

        if "category" in args:
            category = args["category"]
        
        if "vocalized" in args:
            v = False
            if args["vocalized"].lower() == "true":
                v = True
            vocalized = v

    t = []
    needed_count = max_length
    while needed_count > 0:
        res = arrand.arrandom.sample(category=category, vocalized=vocalized, max_length=needed_count)
        res = clean_results(res, category)
        t.extend(res)
        needed_count -= len(res)

    return {
        "result": t
    }

def clean_results(res, category):
    new_res = []
    for r in res:
        if r == '':
            continue
        elif len(r) < 30:
            continue
        elif '****' in r:
            continue
        elif 'a' in r:
            # skip if its in english
            continue

        if '</t>' in r:
            r.replace('</t>', '')
        elif r[-1] == '/':
            r = r[:-1]

        # if string starts with number, remove the number
        if r[:1].isdigit() and category == "poem":
            r = r[2:]

        print(r[-1])

        r.strip()
        r.strip('/')
        r.strip('\/')
        r.strip('\\')
        r.strip(' /')

        new_res.append(r)

    return new_res
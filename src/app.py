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

@app.route("/text")
def text():
    t = arrand.arrandom.select()
    return {
        "result": t
    }

@app.route("/hadith")
def hadith():
    t = arrand.arrandom.hadith()
    return {
        "result": t
    }

@app.route("/aya")
def aya():
    t = arrand.arrandom.aya()
    return {
        "result": t
    }

@app.route("/proverb")
def proverb():
    t = arrand.arrandom.proverb()
    return {
        "result": t
    }

@app.route("/phrase")
def phrase():
    t = arrand.arrandom.phrase()
    return {
        "result": t
    }

@app.route("/poem")
def poem():
    t = arrand.arrandom.poem()
    t = clean_results(t, "poem")
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

        if "paragraphs" in args:
            max_length = int(args["paragraphs"])

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
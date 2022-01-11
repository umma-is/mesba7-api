from flask import Flask
import arrand.arrandom
from flask_cors import CORS
from flask import request


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

    t = arrand.arrandom.sample(category=category, vocalized=vocalized, max_length=max_length)
    return {
        "result": t
    }

from flask import Flask, request, render_template, jsonify
import json
from prompt_processing import tokenizer
from dataextract import textGen

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("hello.html")

@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/textGen", methods=["POST"])
def txt():
    data = request.get_json()
    prompt = data["prompt"]
    result = textGen(prompt)
    print(jsonify(result))
    return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from functions import generate_response
import os
import openai 


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
    authors = ['Earnest Hemingway', 'F Scott Fitzgerald', 'Thucydides', 'Tacitus', 'Thich Nhat Hanh', 'Jane Austin', 'William Shakespeare', 'Marcus Auerelius']
    if request.method == "POST":
        author = request.form["author"]
        text = request.form["text"]
        key = request.form["api_key"]
        openai.api_key = key
        generated_text = generate_response(author, text)
        return redirect(url_for('response', generated_text=generated_text))
    return render_template('index.html', authors=authors)


@app.route('/response')
def response():
    generated_text = request.args.get('generated_text')
    return render_template('response.html', generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)

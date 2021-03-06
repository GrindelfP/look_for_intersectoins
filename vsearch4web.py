from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)
"""I change here something
to do the first commit and push"""


@app.route("/")
def hello() -> str:
    return "Hello world from Flask!"


@app.route("/search4", methods=["POST"])
def do_search() -> "html":
    phrase = request.form["phrase"]
    letters = request.form["letters"]
    return str(search4letters(phrase, letters))


@app.route("/entry")
def entry_page() -> "html":
    return render_template("entry.html", the_title="Velcommen to search4letters on the web!")


app.run(debug=True)

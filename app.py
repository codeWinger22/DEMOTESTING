from flask import Flask, redirect, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
 return "<h1> this is main page</h1>"


if __name__ == "__main__":
 app.run(debug = True)

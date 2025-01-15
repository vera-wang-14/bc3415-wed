from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/") # old style's first line to run

def index(): 
    return(render_template("index.html"))
#do nothing but render template

if __name__ == "__main__":
    app.run()


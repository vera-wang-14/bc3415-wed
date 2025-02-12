from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) # old style's first line to run
def index(): 
    return(render_template("index.html"))
#do nothing but render template


@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    return(render_template("prediction.html"))


@app.route("/predicted_DBS", methods=["GET", "POST"])
def predicted_DBS():
    q = float(request.form.get("q"))
    return(render_template("predicted_DBS.html", r = (-50.6*q)+ 90.2))


if __name__ == "__main__":
    app.run(port=1234)





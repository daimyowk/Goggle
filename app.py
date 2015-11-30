from flask import Flask, render_template, request, redirect
import utils

app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        return render_template("result.html", answer=utils.find_answer(request.form["query"]))
    
if __name__=="__main__":
    app.debug = True
    app.run('0.0.0.0', port=8000)

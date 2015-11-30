from flask import Flask, render_template, request, redirect
import re
import utils

app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        button = request.form['button']
        if button == "Go":
            query = request.form['query']
            if query == "":
                error = "Please ask a question"
                return render_template("home.html", error=error)
            if re.search("(W|w)ho",query)==None and re.search("(W|w)hen",query)==None:
                error = "Please ask a Who or When question"
                return render_template("home.html", error=error)
            return render_template("result.html", answer=utils.find_answer(query))
    
if __name__=="__main__":
    app.debug = True
    app.run('0.0.0.0', port=8000)

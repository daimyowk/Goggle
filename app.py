from flask import Flask, render_template, request, redirect
import utils

app=Flask(__name__)

@app.route('/')

if __name__=="__main__":
    app.debug = True
    app.run('0.0.0.0', port=8000)

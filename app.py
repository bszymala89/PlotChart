from flask import Flask, render_template, request

import plotUtils
import numpy as np

app = Flask(__name__)


@app.route("/")
def helloworld():
    welcome_text = "Hello from server!"

    return welcome_text


@app.route("/chart", methods=["GET", "POST"])
def main():
    
    plotUtils.draw_plot([0,0], "x")

    return render_template("index.html")


@app.route("/chart_post", methods=["GET", "POST"])
def chart_post():
    equation = request.form.get("input")

    plotUtils.draw_plot([1,4], equation)

    return render_template("index.html")


if __name__ == "__main__":
    app.run()


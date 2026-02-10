from flask import Flask, render_template, request

import matplotlib.pyplot as plt
import mathUtils
import numpy as np
import os

app = Flask(__name__)


@app.route("/")
def helloworld():
    welcome_text = "Hello from server!"
    # finalText = re.fullmatch(r"[x0-9 +-*/]", welcomeText.lower())

    return welcome_text


@app.route("/chart", methods=["GET", "POST"])
def main():
    x = 1
    y = 1

    plt.figure()
    plt.plot([x, y], [y, x])
    os.makedirs("static", exist_ok=True)
    plt.savefig("static/chart.png")
    plt.close()

    return render_template("index.html")


@app.route("/chart_post", methods=["GET", "POST"])
def chart_post():
    equation = request.form.get("input")

    x1 = 1
    y1 = mathUtils.calculate_equation(equation, x1)

    x2 = 4
    y2 = mathUtils.calculate_equation(equation, x2)

    plt.figure()
    plt.plot([x1, x2], [y1, y2])
    os.makedirs("static", exist_ok=True)
    plt.savefig("static/chart.png")
    plt.close()

    return render_template("index.html")


if __name__ == "__main__":
    app.run()


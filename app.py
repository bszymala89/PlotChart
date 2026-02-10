from flask import Flask, render_template, request

import matplotlib.pyplot as plt
import mathUtils
import numpy as np
import os

app = Flask(__name__)


@app.route("/")
def helloworld():
    welcomeText = "Hello from server!"
    # finalText = re.fullmatch(r"[x0-9 +-*/]", welcomeText.lower())

    return welcomeText


@app.route("/chart", methods=["GET", "POST"])
def main():
    equasion = request.form.get("input")
    #1. sprowadz do malych liter
    #2. z liter przepusc tylko "x"
    #3. ze operacji matematycznych dozwolone jest "+ - * /"
    #4. dozwolone cyfry to "0,1,2,3,4,5,6,7,8,9"
    #5. spacje muszą być rowniez dozwolone

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
    equasion = request.form.get("input")

    x1 = 1
    y1 = mathUtils.calculateEquasion(equasion, x1)

    x2 = 4
    y2 = mathUtils.calculateEquasion(equasion, x2)

    plt.figure()
    plt.plot([x1, x2], [y1, y2])
    os.makedirs("static", exist_ok=True)
    plt.savefig("static/chart.png")
    plt.close()

    return render_template("index.html")


if __name__ == "__main__":
    app.run()


from flask import Flask, render_template

import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)


@app.route("/")
def helloworld():
    return "Hello from server!"


@app.route("/chart")
def main():
    x = [1,3,5]
    y = [2,4,7]

    plt.figure()
    plt.plot(x, y)
    os.makedirs("static", exist_ok=True)
    plt.savefig("static/chart.png")
    plt.close()
    return render_template("index.html")


if __name__ == "__main__":
    app.run()


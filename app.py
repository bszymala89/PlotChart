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
    plt.figure()
    plt.plot([0], [0])
    os.makedirs("static", exist_ok=True)
    plt.savefig("static/chart.png")
    plt.close()

    return render_template("index.html")

@app.route("/draw")
def draw():
    return "draw"

if __name__ == "__main__":
    app.run()


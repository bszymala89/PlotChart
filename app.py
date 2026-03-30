import base64
import io

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from flask import Flask, render_template, request, jsonify
from models.plotData import PlotData

import mathUtils
import numpy as np

app = Flask(__name__, template_folder=".", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/plot", methods=["POST"])
def plot():
    plots = request.get_json()

    fig, ax = plt.subplots()

    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.grid(True, linestyle="--", alpha=0.5)

    ax.set_xlim([-20, 20])
    ax.set_ylim([-20, 20])

    fig.set_figheight(6)
    fig.set_figwidth(6)

    for p in plots:
        pd = PlotData(
            p["equation"],
            p["color"],
            p["min_x"],
            p["max_x"]
        )

        x_values = mathUtils.convert_str_to_list(pd.min_x, pd.max_x)
        y_values = [mathUtils.calculate_equation(pd.equation, x) for x in x_values]

        ax.plot(x_values, y_values, color=pd.color, label=f"y= {pd.equation}")
    
    ax.legend()
    buf = io.BytesIO()

    fig.savefig(buf, format="png")
    plt.close(fig)

    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode("utf-8")

    return jsonify({"image": image_base64})


if __name__ == "__main__":
    app.run(debug=True)
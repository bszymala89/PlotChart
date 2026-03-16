from flask import Flask, render_template, request
from models.plotData import PlotData

import plotUtils
import mathUtils
import numpy as np

app = Flask(__name__)

data_list = []

@app.route("/")
def helloworld():
    welcome_text = "Hello from server!"

    return welcome_text


@app.route("/chart", methods=["GET", "POST"])
def main():
    global data_list

    plotUtils.draw_plot(PlotData("x", "blue", "0", "0"))

    plot_data = [vars(data) for data in data_list]

    return render_template("index.html", plot_data=plot_data)


@app.route("/chart_post", methods=["GET", "POST"])
def chart_post():
    global data_list

    data = PlotData(
        request.form.get("input"),
        request.form.get("color_input"),
        request.form.get("min_x_input"),
        request.form.get("max_x_input")
        )

    data_list.append(data)

    for i in data_list:
        plotUtils.draw_plot(i)

    plot_data = [vars(data) for data in data_list]

    return render_template("index.html", plot_data=plot_data)


if __name__ == "__main__":
    app.run()
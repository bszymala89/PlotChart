from flask import Flask, render_template, request

import plotUtils
import mathUtils
import numpy as np

app = Flask(__name__)


@app.route("/")
def helloworld():
    welcome_text = "Hello from server!"

    return welcome_text


@app.route("/chart", methods=["GET", "POST"])
def main():
    
    plotUtils.draw_plot([0,0], "x", "blue")

    return render_template("index.html")


@app.route("/chart_post", methods=["GET", "POST"])
def chart_post():
    equation = request.form.get("input")
    min_x = request.form.get("min_x_input")
    max_x = request.form.get("max_x_input")

    color = request.form.get("color_input")

    plotUtils.draw_plot(mathUtils.convert_str_to_list(min_x, max_x), equation, color)

    return render_template("index.html")


if __name__ == "__main__":
    app.run()

# 1. Przycisk do rysowania


# 2, Zakres rysowania wykresu ( od jakiego x do jakiego x)
# 3. Przycisk + zeby dodac kolejny wykres liniowy na charcie


# 4. Zmiana koloru wykresu
# 1 -> 4 -> 2 -> 3

# https://getcssscan.com/css-buttons-examples
import matplotlib.pyplot as plt
import mathUtils
import os


def draw_plot(table_x: list, equation: str, color):
    table_y = []

    for x in table_x:
        table_y.append(mathUtils.calculate_equation(equation, x))
        

    plt.figure(facecolor="#999999", dpi=150)
    plt.plot(table_x, table_y, color=color)
    os.makedirs("static", exist_ok=True)
    plt.savefig("static/chart.png")
    plt.close()
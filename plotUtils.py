from models.plotData import PlotData

import matplotlib.pyplot as plt
import mathUtils
import os


def draw_plot(data: PlotData):
    table_y = []
    table_x = mathUtils.convert_str_to_list(data.min_x, data.max_x)

    for x in table_x:
        table_y.append(mathUtils.calculate_equation(data.equation, x))
        

    plt.figure(facecolor="#999999", dpi=150)
    plt.plot(table_x, table_y, color=data.color)
    os.makedirs("static", exist_ok=True)
    plt.savefig("static/chart.png")
    plt.close()
from models.plotData import PlotData
from io import BytesIO
import matplotlib.pyplot as plt
import mathUtils
import os

MAX_X = 20
MIN_X = -20
MAX_Y = 20
MIN_Y = -20


def draw_plots(data_list):
    fig, ax = plt.subplots(facecolor="white", dpi=200)
    
    for data in data_list:
        table_x = mathUtils.convert_str_to_list(MIN_X, MAX_X)
        table_y = [mathUtils.calculate_equation(data.equation, x) for x in table_x]
        ax.plot(table_x, table_y, color=data.color)

    ax.set_xlim(MIN_X, MAX_X)
    ax.set_ylim(MIN_Y, MAX_X) 

    ax.grid(True)

    ax.set_xlabel("x")
    ax.set_ylabel("y")

    return fig

    

def render_plot_image(data_list):
    fig = draw_plots(data_list)
    buffer = BytesIO()

    fig.savefig(buffer, format="png")
    plt.close(fig)

    return buffer
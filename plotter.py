import pandas as pd
from pandas import read_csv
from scipy.optimize import curve_fit
from typing import List, Tuple
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


FIGURE_WIDTH = 12
FIGURE_HEIGHT = 12
DOUBLE_FIGURE_HEIGHT = 20
FONT = "Arial"
FONT_WEIGHT = "bold"
FONT_SIZE = 22
LINE_WIDTH = 3

# matplotlib settings
mpl.rcParams['font.family'] = FONT
mpl.rcParams['font.weight'] = FONT_WEIGHT
plt.rcParams['font.size'] = FONT_SIZE
plt.rcParams['axes.linewidth'] = LINE_WIDTH

def print_fit_data(objective, popt, pcov):
    perr = np.sqrt(np.diag(pcov))
    print(f"printing [{objective.__name__}] fitting values")
    for i, var in enumerate(objective.__code__.co_varnames[1:]):
        if (i == objective.__code__.co_argcount - 1):
            break
        print(f"parameter {var} = {popt[i]}, with std={perr[i]}")


def plot_data(x_data: pd.DataFrame,
              y_data: pd.DataFrame,
              fit_function=None,
              starting_points: List[float] = None,
              bounds: Tuple[Tuple, Tuple] = (-np.inf, np.inf),
              residuals: bool = True,
              save: bool = False):

    # graph parameters
    x_data_name = x_data.name.split()[0]
    x_data_units = x_data.name.split()[1]
    y_data_name = y_data.name.split()[0]
    y_data_units = y_data.name.split()[1]

    # fit
    popt, pcov = curve_fit(f=fit_function, xdata=x_data, ydata=y_data, p0=starting_points, bounds=bounds)
    fit = fit_function(x_data, *popt)
    print_fit_data(fit_function, popt, pcov)
    residuals_graph = y_data - fit

    # show graphs
    if residuals:
        plt.rcParams["figure.figsize"] = (FIGURE_WIDTH, DOUBLE_FIGURE_HEIGHT)

        fig, ax = plt.subplots(2)
        graph_ax = ax[0]
        residuals_ax = ax[1]
    else:
        plt.rcParams["figure.figsize"] = (FIGURE_WIDTH, FIGURE_HEIGHT)

        fig, graph_ax = plt.subplots(1)

    fig.tight_layout(pad=4.0)
    graph_ax.plot(x_data, y_data, 'o', markersize=7, markeredgewidth=1, color='blue', markerfacecolor='lightskyblue',
               label='Measurement')
    graph_ax.plot(x_data, fit, '-', color='red', label="Fit", linewidth=3)
    graph_ax.set_xlabel(f'${x_data_name} {x_data_units}$', fontsize=26)
    graph_ax.set_ylabel(f'${y_data_name} {y_data_units}$', fontsize=26)
    graph_ax.set_title(f"{y_data_name} Measured as function of {x_data_name}", fontname="Arial", size=32, fontweight="bold")
    graph_ax.legend(loc='best')
    graph_ax.grid()

    if residuals:
        residuals_ax.stem(x_data, residuals_graph, label='Residuals', linefmt='black')
        residuals_ax.set_title("Residuals Graph", fontname="Arial", size=32, fontweight="bold")
        residuals_ax.set_xlabel(f'${x_data_name} {x_data_units}$', fontsize=26)
        residuals_ax.set_ylabel(f'${y_data_name} {y_data_units}$', fontsize=26)
        residuals_ax.grid()

    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)

    if save:
        plt.savefig(f"graph: {y_data.name} as function of {x_data.name}", dpi=300)
    else:
        plt.show()


if __name__ == "__main__":
    data_path = './../data/rlc_analyzed.csv'
    # unpack data
    data_frame = read_csv(data_path)

    phase = -data_frame["Phase [rad]"]
    amplitude = data_frame["Amplitude [V]"]
    frequency = data_frame["Frequency [KHz]"]
    def fit_function(x, a, b, c):
        return -np.arctan((a * x - 1 / (b * x)) / (1.618)) + c


    starting_points = [0.2769, 0.0003, 0]
    bounds = ((-100, -np.inf, -np.inf), (np.inf, np.inf, np.inf))

    plot_data(frequency, phase, fit_function, starting_points=starting_points, bounds=bounds, residuals=True, save=False)

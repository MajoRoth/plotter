import pandas as pd
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
from pandas import read_csv
from scipy.optimize import curve_fit, least_squares
from typing import List, Tuple
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


FIGURE_WIDTH = 12
FIGURE_HEIGHT = 12
DOUBLE_FIGURE_HEIGHT = 18
FONT = "Arial"
FONT_WEIGHT = "bold"
FONT_SIZE = 22
LINE_WIDTH = 3

# matplotlib settings
mpl.rcParams['font.family'] = FONT
mpl.rcParams['font.weight'] = FONT_WEIGHT
plt.rcParams['font.size'] = FONT_SIZE
plt.rcParams['axes.linewidth'] = LINE_WIDTH


def print_fit_data(fit, popt, pcov, xdata, ydata, normal_vec):
    perr = np.sqrt(np.diag(pcov))

    if normal_vec is None:
        normal_vec = np.zeros(len(popt))

    real_popt = np.multiply(
        np.power(10, normal_vec),
        popt
    )
    residuals = ydata - fit(xdata, *real_popt)
    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((ydata - np.mean(ydata)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)
    k = 0

    print('\033[96m' + f"printing function [{fit.__name__}] fitting values" + "\033[0m")
    print('\033[1m' + "parameter    value           std         normal factor" + "\033[0m")
    for i, var in enumerate(fit.__code__.co_varnames[1:]):
        if (i == fit.__code__.co_argcount - 1):
            break
        k += 1
        print("{:<12.5} {:<15.4} {:<10.4}  {:<10.6}".format(var, popt[i], perr[i], normal_vec[i]))

    n = len(xdata)  # num of observations
    adjusted_r = 1 - (
            (1 - r_squared) * (n - 1) / (n - k - 1)
    )
    print('\033[92m' + f"printing fit parameters R^2: [{r_squared}] adjusted R^2: [{adjusted_r}]" + "\033[0m")


def order_of_magnitude(number):
    return np.floor(np.log10(number))


def plot_data(x_data: pd.DataFrame,
              y_data: pd.DataFrame,
              fit_function=None,
              starting_points: List[float] = None,
              bounds: Tuple[Tuple, Tuple] = (-np.inf, np.inf),
              residuals: bool = True,
              graph_dir_path: str = None,
              experiment_name: str = ""):
    # graph parameters
    try:
        x_data_name = x_data.name.split()[0]
        x_data_units = x_data.name.split()[1]
    except:
        x_data_name = x_data.name
        x_data_units = ""
    try:
        y_data_name = y_data.name.split()[0]
        y_data_units = y_data.name.split()[1]
    except:
        y_data_name = y_data.name
        y_data_units = ""

    # fit
    if fit_function is not None:
        if starting_points is not None:
            magnitude_list = order_of_magnitude(starting_points)
            normalized_starting_points = np.multiply(
                np.power(10, (-1) * magnitude_list),
                starting_points
            )

            def fit_function_normalizer(x, *args):
                real_arguments = np.multiply(
                    np.power(10, magnitude_list),
                    args
                )
                return fit_function(x, *real_arguments)

        else:
            normalized_starting_points = None
            normalized_bounds = None
            fit_function_normalizer = fit_function
            magnitude_list = None

        popt, pcov = curve_fit(f=fit_function_normalizer, xdata=x_data, ydata=y_data, p0=normalized_starting_points,
                               bounds=bounds, maxfev=5000)
        x_sample = np.linspace(x_data.iloc[0], x_data.iloc[-1], 1000)
        try:
            real_popt = np.multiply(
                np.power(10, magnitude_list),
                popt
            )
        except:
            real_popt = popt

        fit = fit_function(x_sample, *real_popt)
        fit_for_residuals = fit_function(x_data, *real_popt)
        print_fit_data(fit_function, popt, pcov, x_data, y_data, magnitude_list)
        residuals_graph = y_data - fit_for_residuals
    else:
        # Cannot create residuals without fit
        residuals = False

    # show graphs
    if residuals:
        fig, ax = plt.subplots(2, 1, figsize=(FIGURE_WIDTH, DOUBLE_FIGURE_HEIGHT),
                               gridspec_kw={'height_ratios': [2, 1]})
        graph_ax = ax[0]
        residuals_ax = ax[1]
    else:
        plt.rcParams["figure.figsize"] = (FIGURE_WIDTH, FIGURE_HEIGHT)
        fig, graph_ax = plt.subplots(1)

    fig.tight_layout(pad=4.0)
    graph_ax.plot(x_data, y_data, 'o', markersize=5, markeredgewidth=1, color='blue', markerfacecolor='lightskyblue',
                  label='Measurement')

    if fit_function is not None:
        graph_ax.plot(x_sample, fit, '-', color='red', label="Fit", linewidth=3)
    graph_ax.set_xlabel(f'${x_data_name} {x_data_units}$', fontsize=26)
    graph_ax.set_ylabel(f'${y_data_name} {y_data_units}$', fontsize=26)
    graph_ax.set_title(f"${y_data_name}~Measured~as~Function~of~{x_data_name}$", fontname="Arial", size=32,
                       fontweight="bold")
    graph_ax.legend(loc='best')
    graph_ax.grid()

    if residuals:
        residuals_ax.stem(x_data, residuals_graph, label='Residuals', linefmt='black')
        residuals_ax.set_title("Residuals Graph", fontname="Arial", size=32, fontweight="bold")
        residuals_ax.set_xlabel(f'${x_data_name} {x_data_units}$', fontsize=26)
        residuals_ax.set_ylabel(f'${y_data_name} {y_data_units}$', fontsize=26)
        residuals_ax.grid()


    if graph_dir_path is None or experiment_name is None:
        plt.show()
    else:
        plt.savefig(f"{graph_dir_path}/{experiment_name}-{y_data.name}-{x_data.name}.eps"
                    .replace(" ", "_").replace("{", "").replace("}", ""), format="eps")


def plot_comparison(data_list: List[Tuple[pd.DataFrame, pd.DataFrame, str]],
                    graph_dir_path: str = None,
                    experiment_name: str = ""):
    COLORS = ["red", "blue", "orange", "pink", "green", "purple"]

    main_data = data_list[0]
    try:
        x_data_name = main_data[0].name.split()[0]
        x_data_units = main_data[0].name.split()[1]
    except:
        x_data_name = main_data[0].name
        x_data_units = ""
    try:
        y_data_name = main_data[1].name.split()[0]
        y_data_units = main_data[1].name.split()[1]
    except:
        y_data_name = main_data[1].name
        y_data_units = ""

    plt.rcParams["figure.figsize"] = (FIGURE_WIDTH, FIGURE_HEIGHT)
    fig, graph_ax = plt.subplots(1)

    fig.tight_layout(pad=4.0)
    for i, data in enumerate(data_list):
        graph_ax.plot(data[0], data[1], '-', color=COLORS[i],
                      label=f'${data[2]}$')

    graph_ax.grid()

    graph_ax.set_xlabel(f'${x_data_name} {x_data_units}$', fontsize=26)
    graph_ax.set_ylabel(f'${y_data_name} {y_data_units}$', fontsize=26)
    graph_ax.set_title(f"$|H|~Measured~as~Function~of~{x_data_name}$", fontname="Arial", size=32,
                       fontweight="bold")
    graph_ax.legend(loc='best')



    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)

    if graph_dir_path is None or experiment_name is None:
        plt.show()
    else:
        plt.savefig(f"{graph_dir_path}/{experiment_name}-{main_data[1].name}-{main_data[0].name}.eps"
                    .replace(" ", "_").replace("{", "").replace("}", ""), format="eps")




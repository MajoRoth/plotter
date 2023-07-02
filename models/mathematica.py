import pandas
import numpy as np
from plotter import plot_data, plot_comparison
import matplotlib.pyplot as plt
import matplotlib as mpl


import scipy.integrate as integrate

# Data Settings

name = None


def poly(x, M):

    # R1 = 0.5
    # R2 = 12
    #
    #
    # w = 2 * np.pi * x
    #
    # L1 = 0.3526 * 10 ** (-4)
    # L2 = 2.553 * 10 ** (-3)
    # C2 = 2.75 * 19 ** (-10)
    # Cs = 61.49 * 10 ** (-10)

    C1 = 13.4 * 10 ** (-11)
    C2 = C1
    R1 = 15
    R2 = 16
    Cs = 1.72 * 10 ** (-11)
    L1 = 1.6 * 10 ** (-3)
    L2 = 0.91 * 10 ** (-3)
    w = 2 * np.pi * x * 1000

    return M*w*(w**2*(L1+(C2+Cs)*R1*R2+(C2+Cs)*((-1)*L1*L2+M**2)*w**2)**2+(R1+(-1)*(C2+Cs)*(L2*R1+L1*R2)*w**2)**2)**(-1/2)

columns = list()

M = np.array([52, 35, 18, 13, 7, 5]) * 10 ** (-5)
CM = [0, 5, 11, 14, 20, 24]
x = np.linspace(400, 550, 1000)



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


COLORS = ["red", "blue", "orange", "pink", "green", "purple"]

plt.rcParams["figure.figsize"] = (FIGURE_WIDTH, FIGURE_HEIGHT)
fig, graph_ax = plt.subplots(1)


print(columns)


for i, m in enumerate(M):
    graph_ax.plot(x, poly(x, m), '-', color=COLORS[i],
                  label=f'${CM[i]} [cm]$')


graph_ax.grid()

graph_ax.set_xlabel(f'$Frequency [kHz]$', fontsize=26)
graph_ax.set_ylabel(f'$|H|$', fontsize=26)
graph_ax.set_title(f"$|H|~Measured~as~Function~of~Frequency$", fontname="Arial", size=32, fontweight="bold")
graph_ax.legend(loc='best')

plt.show()




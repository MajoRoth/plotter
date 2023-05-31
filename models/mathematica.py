import pandas
import numpy as np
from plotter import plot_data

# Data Settings
data_path = './../data/picoscope_internal_resistance_measurement_1KOhm.csv'

experiment_name="internal_resistance"


def poly(x):
     x = x / 100
     a = 0.0005239231436759905
     b = - 0.11162988067784889
     c = 28.779375241469147
     d = - 5501.016162472724
     e = 594099.1623342653
     f = - 3.2256761250060298e7
     g = 8.008527125777614e8
     h = - 7.772880951154212e9
     i = 2.023257941657045e10
     const = 693.2804257303192

     return const * (a
                     + b * x ** 2
                     + c * x ** 4
                     + d * x ** 6
                     + e * x ** 8
                     + f * x ** 10
                     + g * x ** 12
                     + h * x ** 14
                     + i * x ** 16)

# preprocess data
x = np.linspace(0, 9.5, 1000)
y = poly(x)
d = {'distance [cm]': x, 'k': y}
df = pandas.DataFrame(data=d)

y_col = df["k"]
x_col = df["distance [cm]"]





plot_data(x_col, y_col, graph_dir_path="./../graphs", experiment_name="coupling_coeff")



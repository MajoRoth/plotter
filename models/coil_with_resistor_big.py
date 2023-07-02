import os
import sys

import numpy as np
from pandas import read_csv
from plotter import plot_data

# Data Settings
data_path = './../data/R=47kOhm(big).csv'
CIRCUIT_NAME = None # "coil_resistor_47"
# CIRCUIT_NAME = None
# unpack data
data_frame = read_csv(data_path)


phase = data_frame["phase [rad]"]
amplitude = data_frame["amplitude"]
frequency = data_frame["frequency [Hz]"] / 1000
frequency.name = "frequency [kHz]"
frequency = frequency


def amplitude_to_freq_r_fit(x, L_c, C_c, R_cl, C_s, const):
    # Constants
    # C_s = 63 * 10 ** (-12)
    R_ext = 47000

    # Normalize
    # C_s = C_s * 5.5 * 10 ** (-11)
    # C_c = C_c * 10 ** (-10)
    # L_c = L_c * 10 ** (-3)

    R_cp = np.inf
    R_cc = 0

    w = 2 * np.pi * x * 1000

    Z = R_ext
    Z_measure = (1/Z + 1j * w * C_s) ** (-1)
    Z_coil = (1 / (R_cl + 1j * w * L_c ) + 1 / (R_cc + 1 / (1j * w * C_c) + 1 / R_cp)) ** (-1)

    return np.absolute(Z_measure / (Z_coil + Z_measure)) + const

# big coil starting parameters
# starting_point = [0.0034, 1.9 * 10 ** (-10), 40, 63 * 10 ** (-12)]
starting_point = [0.001917, 34.23 * 10 ** (-11), 67.23, 9.61 * 10 ** (-11), 0.001]
bounds = [[0, 0, 0, 0, -np.inf], [np.inf, np.inf, np.inf, np.inf, np.inf]]

plot_data(frequency, amplitude, graph_dir_path="./../graphs", experiment_name=CIRCUIT_NAME, bounds=bounds)


def phase_to_freq_r_fit(x, L_c, C_c, R_cl, C_s, const):
    # C_s = 63 * 10 ** (-12)
    R_ext = 47000

    R_cp = np.inf
    R_cc = 0

    w = 2 * np.pi * x * 1000
    Z = R_ext
    Z_measure = (1 / Z + 1j * w * C_s) ** (-1)
    Z_coil = (1 / (R_cl + 1j * w * L_c) + 1 / (R_cc + 1 / (1j * w * C_c) + 1 / R_cp)) ** (-1)
    Z_coil = (1 / (R_cl + 1j * w * L_c) + 1j * w * C_c) ** (-1)

    return -np.angle(Z_measure / (Z_coil + Z_measure)) + const

# starting_point = [0.001377, 10.59 * 10 ** (-11), 81.52, 0.1, 10 ** 5, 0.001]
# bounds = ((0, 0, 0, 0, 0, 0), (np.inf, np.inf, np.inf, np.inf, np.inf, 5))
#
# starting_point = [0.0029, 4.95 * 10 ** (-11), 174.52, 42 * 10 ** (-12), 0.1]
# bounds = [[0, 0, 0, 0, 0], [np.inf, np.inf, np.inf, np.inf, np.inf]]

plot_data(frequency, phase, starting_points=starting_point,
           graph_dir_path="./../graphs", experiment_name=CIRCUIT_NAME)

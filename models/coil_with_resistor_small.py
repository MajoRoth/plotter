import os
import sys

import numpy as np
from pandas import read_csv
from plotter import plot_data

# Data Settings
data_path = './../data/coil_with_resistor_22kohm.csv'
CIRCUIT_NAME = "coil_resistor_22"
# CIRCUIT_NAME = None
# unpack data
data_frame = read_csv(data_path)


phase = data_frame["phase [rad]"][:120]
amplitude = data_frame["amplitude"][:120]
frequency = data_frame["frequency [Hz]"] / 1000
frequency.name = "frequency [kHz]"
frequency = frequency[:120]


def amplitude_to_freq_r_fit(x, L_c, C_c, R_cl, const, C_s):
    # Constants
    # C_s = 63 * 10 ** (-12)
    R_ext = 22000

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
starting_point = [0.0029, 4.95 * 10 ** (-11), 174.52, 0.08, 42 * 10 ** (-12)]
bounds = [[0, 0, 0, 0, 0], [np.inf, np.inf, np.inf, np.inf, np.inf]]

plot_data(frequency, amplitude, fit_function=amplitude_to_freq_r_fit, starting_points=starting_point,
            graph_dir_path="./../graphs", experiment_name=CIRCUIT_NAME, bounds=bounds)


def phase_to_freq_r_fit(x, L_c, C_c, R_cl, C_s):
    # C_s = 63 * 10 ** (-12)
    R_ext = 22000

    R_cp = np.inf
    R_cc = 0

    w = 2 * np.pi * x * 1000
    Z = R_ext
    Z_measure = (1 / Z + 1j * w * C_s) ** (-1)
    Z_coil = (1 / (R_cl + 1j * w * L_c) + 1 / (R_cc + 1 / (1j * w * C_c) + 1 / R_cp)) ** (-1)
    Z_coil = (1 / (R_cl + 1j * w * L_c) + 1j * w * C_c) ** (-1)

    return -np.angle(Z_measure / (Z_coil + Z_measure))

# starting_point = [0.001377, 10.59 * 10 ** (-11), 81.52, 0.1, 10 ** 5, 0.001]
# bounds = ((0, 0, 0, 0, 0, 0), (np.inf, np.inf, np.inf, np.inf, np.inf, 5))

starting_point = [10 ** (-3), 65 * 10 ** (-12), 100, 65 * 10 ** (-12)]
bounds = [[0, 0, 0, 0], [np.inf, np.inf, np.inf, np.inf]]

plot_data(frequency, phase, fit_function=phase_to_freq_r_fit, starting_points=starting_point, bounds=bounds,
           graph_dir_path="./../graphs", experiment_name=CIRCUIT_NAME)

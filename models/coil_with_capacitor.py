import numpy as np
from pandas import read_csv
from plotter import plot_data

# Data Settings
data_path = './../data/C=1e-10F_R=47kOhm(big).csv'
# data_path = './../data/C=1e-10F_R=47kOhm(small).csv'
# unpack data
data_frame = read_csv(data_path)

# CIRCUIT_NAME = "coil_capacitor_47_big"
CIRCUIT_NAME = None

phase = data_frame["phase [rad]"]
amplitude = data_frame["amplitude"]
frequency = data_frame["frequency [Hz]"] / 1000
frequency.name = "frequency [kHz]"


def amplitude_to_freq_r_fit(x, L_c, C_c, R_cl, C_s):
    # C_s = 5.5 * 10 ** (-11)
    R_ext = 470000
    C_ext = 10 ** (-10)

    R_cp = np.inf
    R_cc = 0

    w = 2 * np.pi * x * 1000

    Z = R_ext
    Z_measure = (1/Z + 1j * w * C_s) ** (-1)
    Z_coil = (1 / (R_cl + 1j * w * L_c) + 1 / (R_cc + 1 / (1j * w * C_c)) + 1 / R_cp + 1j * w * C_ext) ** (-1)

    return np.absolute(Z_measure / (Z_coil + Z_measure))

starting_point = [0.00225, 343 * 10 ** (-12), 458, 7.5 * 10 ** (-12)]
bounds = ((0, 0, 0, 0), np.array(starting_point) * 10000)

plot_data(frequency, amplitude, fit_function=amplitude_to_freq_r_fit, starting_points=starting_point, bounds=bounds,
           graph_dir_path="./../graphs", experiment_name=CIRCUIT_NAME)


def phase_to_freq_r_fit(x, L_c, C_c, R_cl, C_s):
    # C_s = 5.5 * 10 ** (-11)
    R_ext = 470000
    C_ext = 10 ** (-10)

    R_cp = np.inf
    R_cc = 0

    w = 2 * np.pi * x * 1000

    Z = R_ext
    Z_measure = (1 / Z + 1j * w * C_s) ** (-1)
    Z_coil = (1 / (R_cl + 1j * w * L_c) + 1 / (R_cc + 1 / (1j * w * C_c)) + 1 / R_cp + 1j * w * C_ext) ** (-1)

    return np.angle(Z_measure / (Z_coil + Z_measure))

starting_point = [0.00225, 343 * 10 ** (-12), 458, 7.5 * 10 ** (-12)]
bounds = ((0, 0, 0, 0), (np.inf, np.inf, np.inf, np.inf))

plot_data(frequency, phase, fit_function=phase_to_freq_r_fit, starting_points=starting_point,
           graph_dir_path="./../graphs", experiment_name=CIRCUIT_NAME)

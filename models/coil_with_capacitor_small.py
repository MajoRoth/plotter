import numpy as np
from pandas import read_csv
from plotter import plot_data

# Data Settings
data_path = './../data/C=1e-10F_R=47kOhm(small).csv'
# unpack data
data_frame = read_csv(data_path)

CIRCUIT_NAME = "coil_capacitor_47_small"
CIRCUIT_NAME = None

phase = data_frame["phase [rad]"]
amplitude = data_frame["amplitude"]
amplitude = 1 / amplitude
frequency = data_frame["frequency [Hz]"] / 1000
frequency.name = "frequency [kHz]"


def amplitude_to_freq_r_fit(x, L_c, C_c, R_cl, C_s, const):
    # C_s = 5.5 * 10 ** (-11)
    # L_c, C_c, R_cl, C_s, const = [0.002134, 29.18 * 10 ** (-11), 53.78, 8.601 * 10 ** (-11), 0.001233]
    R_ext = 22000
    C_ext = 10 ** (-10)

    R_cp = np.inf
    R_cc = 0

    w = 2 * np.pi * x * 1000

    Z = R_ext
    Z_measure = (1/Z + 1j * w * C_s) ** (-1)
    Z_coil = (1 / (R_cl + 1j * w * L_c) + (1j * w * C_c) + 1 / R_cp + 1j * w * C_ext) ** (-1)

    return np.absolute(Z_measure / (Z_coil + Z_measure)) + const

starting_point = [0.001377, 10.59 * 10 ** (-11), 81.52, 9.005 * 10 ** (-11), 0.0081]
bounds = [[0, 0, 0, 0, -np.inf], [np.inf, np.inf, np.inf, np.inf, np.inf]]

plot_data(frequency, amplitude, fit_function=amplitude_to_freq_r_fit, starting_points=starting_point, bounds=bounds,
           graph_dir_path="./../graphs", experiment_name=CIRCUIT_NAME)


def phase_to_freq_r_fit(x, L_c, C_c, R_cl, C_s, const):
    # C_s = 5.5 * 10 ** (-11)
    R_ext = 470000
    C_ext = 10 ** (-10)

    R_cp = np.inf
    R_cc = 0

    w = 2 * np.pi * x * 1000

    Z = R_ext
    Z_measure = (1 / Z + 1j * w * C_s) ** (-1)
    Z_coil = (1 / (R_cl + 1j * w * L_c) + 1 / (R_cc + 1 / (1j * w * C_c)) + 1 / R_cp + 1j * w * C_ext) ** (-1)

    return -np.angle(Z_measure / (Z_coil + Z_measure)) + const


plot_data(frequency, phase, fit_function=phase_to_freq_r_fit, starting_points=starting_point, bounds=bounds,
           graph_dir_path="./../graphs", experiment_name=CIRCUIT_NAME)

import numpy as np
from pandas import read_csv
from plotter import plot_data

# Data Settings
data_path = './../data/L=1mH(small).csv'
# unpack data
data_frame = read_csv(data_path)

phase = data_frame["phase [rad]"]
amplitude = data_frame["amplitude"]
frequency = data_frame["frequency [Hz]"] / 1000
frequency.name = "frequency [kHz]"


def amplitude_to_freq_r_fit(x, L_c, C_c, R_cl):
    # C_s = 32.4 * 10 ** (-12)
    C_s = 5.5 * 10 ** (-11)
    R_ext = 470000
    L_ext = 10 ** (-3)

    R_cp = np.inf
    R_cc = 0
    # R_cl = 0.001
    # L_c = 0.0039
    # C_c = 1.14 * 10 ** (-11)


    w = 2 * np.pi * x * 1000

    Z = 1j * w * L_ext
    Z_measure = (1/Z + 1j * w * C_s) ** (-1)

    Z_coil = (1 / (R_cl + 1j * w * L_c) + 1 / (R_cc + 1 / (1j * w * C_c)) + 1 / R_cp) ** (-1)


    # R, L, C = [1, 5 ** (-3), 10 ** (-11)]
    # numerator = (1/R_ext + w * C_s * 1j ) ** (-1)
    # Z_c = (1/(Rc + 1/(w * C * 1j)) + 1/(Rl + w * L * 1j)) ** (-1)
    # denominator = Z_c + numerator + R_s
    return np.absolute(Z_measure / (Z_coil + Z_measure))

# starting_point = [0.00378,  3.89 * 10 ** (-11), 100, 10 ** (-12)]
starting_point = [4 * 0.00378, 3.89 * 10 ** (-11), 200]

bounds = ((0, 0, 0, 0), (np.inf, np.inf, np.inf, np.inf))

plot_data(frequency, amplitude, fit_function=amplitude_to_freq_r_fit, starting_points=starting_point,
           graph_dir_path="./../graphs", experiment_name=None)

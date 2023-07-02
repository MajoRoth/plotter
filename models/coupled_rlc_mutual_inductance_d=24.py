from pandas import read_csv
from plotter import plot_data
import numpy as np

# Data Settings
data_path = './../data/d=24.csv'

# preprocess data
data_frame = read_csv(data_path)

filtered_data_frame = data_frame[data_frame["Frequency [Hz]"] >= 1]

a = filtered_data_frame["Amplitude"]
phase = filtered_data_frame["Phase [rad]"]
freq = filtered_data_frame["Frequency [Hz]"]
freq = freq / 1000
freq.name = "Frequency [kHz]"

experiment_name = "coupled_d=24"


def amplitude_to_freq_fit(x, m, L1, L2, C1, Cs, R1, R2, const):
    Rext = 47000
    # R1 = 57
    # R2 = 70

    # k, L1, L2, C1, Cs, R1, R2 = [0.4474, 0.0022, 0.00067, 26.58 * 10 ** (-11), 10 ** (-10), 90, 32.92]

    k = m / np.sqrt(L1 * L2)

    w = 2 * np.pi * x * 1000

    ret = w * k * np.sqrt(L1 * L2) * np.sqrt((1 + Cs ** 2 * w ** 2 * Rext ** 2) / (
            (w * (L1 + C1 * R1 * R2 + Cs * R1 * Rext + C1 * (R1 + R2) * Rext)
             - C1 * w ** 3 * (
                     L1 * L2 - k ** 2 * L1 * L2 + (C1 + Cs) * (L2 * R1 + L1 * R2) * Rext)) ** 2 +
            (R1 + Rext + w ** 4 * C1 * (C1 + Cs) * (
                    L1 * L2 - k ** 2 * L1 * L2) * Rext - w ** 2 * (
                     C1 * (L2 * R1 + L1 * R2)
                     + (C1 * L1 + Cs * L1 + C1 * L2 + C1 * (C1 + Cs) * R1 * R2) * Rext)) ** 2))

    return ret + const


starting_point = [0.05 * 10 ** (-3), 0.6 * 10 ** (-3), 1.8 * 10 ** (-3),
                  36.05 * 10 ** (-11), 9.2 * 10 ** (-11),
                  59.18, 78.38, 0.01]

bounds = [(0, 0, 0, 0, 0, 0, 0, -np.inf), (np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf)]

plot_data(freq, a, fit_function=amplitude_to_freq_fit, starting_points=starting_point, bounds=bounds,
          graph_dir_path="./../graphs", experiment_name=experiment_name)

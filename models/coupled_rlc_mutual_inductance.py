from pandas import read_csv
from plotter import plot_data
import numpy as np

# Data Settings
data_path = './../data/coupeled_again.csv'
data_path = "./../data/coupeled_R=47kOhm.csv"

# preprocess data
data_frame = read_csv(data_path)

filtered_data_frame = data_frame[data_frame["Frequency [Hz]"] >= 1]

a = filtered_data_frame["Amplitude"]
phase = filtered_data_frame["Phase [rad]"]
freq = filtered_data_frame["Frequency [Hz]"]
freq = freq / 1000
freq.name = "Frequency [kHz]"

experiment_name = None # "mutual_inductance"


def amplitude_to_freq_fit(x, k, L1, L2, C1, Cs, R1, R2):
    Rext = 47000
    # R1 = 57
    # R2 = 70

    # k, L1, L2, C1, Cs, R1, R2 = [0.4474, 0.0022, 0.00067, 26.58 * 10 ** (-11), 10 ** (-10), 90, 32.92]

    w = 2 * np.pi * x * 1000

    ret = w * k * np.sqrt(L1 * L2) * np.sqrt((1 + Cs ** 2 * w ** 2 * Rext ** 2) / (
            (w * (L1 + C1 * R1 * R2 + Cs * R1 * Rext + C1 * (R1 + R2) * Rext)
             - C1 * w ** 3 * (
                     L1 * L2 - k ** 2 * L1 * L2 + (C1 + Cs) * (L2 * R1 + L1 * R2) * Rext)) ** 2 +
            (R1 + Rext + w ** 4 * C1 * (C1 + Cs) * (
                    L1 * L2 - k ** 2 * L1 * L2) * Rext - w ** 2 * (
                     C1 * (L2 * R1 + L1 * R2)
                     + (C1 * L1 + Cs * L1 + C1 * L2 + C1 * (C1 + Cs) * R1 * R2) * Rext)) ** 2))

    return ret


starting_point = [0.2, 3.272 * 10 ** (-3), 0.001, 1.52 * 10 ** (-10), 10.17 * 10 ** (-11)]
starting_point = [0.4712, 2.07 * 10 ** (-3), 6.47 * 10 ** (-4), 28.48 * 10 ** (-11), 9.996 * 10 ** (-11), 90, 32.92]
starting_point = [0.4474, 0.0022, 0.00067, 26.58 * 10 ** (-11), 10 ** (-10), 90, 32.92]

bounds = [(0, 0, 0, 0, 0, 0, 0), (np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf)]

plot_data(freq, a, fit_function=amplitude_to_freq_fit, starting_points=starting_point, bounds=bounds,
          graph_dir_path="./../graphs", experiment_name=experiment_name)


def phase_to_freq_fit(x, k, L1, L2, C1, Cs, const):
    Rext = 47000
    R1 = 57
    R2 = 70

    w = 2 * np.pi * x * 1000

    ret = np.pi - abs(np.angle(k * (L1 * L2) ** (1 / 2) * w * ((1j * (-1)) + Cs * Rext * w) * (
                (-1) * Rext + (1j * (-1)) * (L1 + C1 * R2 * Rext) * w + (
                    C1 * L1 * R2 + Cs * L1 * Rext + C1 * (L1 + L2) * Rext) * w ** 2 + 1j * C1 * (
                            (-1) * k ** 2 * L1 * L2 + L1 * (L2 + (C1 + Cs) * R2 * Rext)) * w ** 3 + (-1) * C1 * (
                            C1 + Cs) * (L1 * L2 + (-1) * k ** 2 * L1 * L2) * Rext * w ** 4 + R1 * (
                            (1j * (-1)) + (C1 + Cs) * Rext * w) * (
                            (1j * (-1)) + C1 * w * (R2 + 1j * L2 * w))) ** (-1)))
    return ret + const

bounds = [(0, 0, 0, 0, 0, -np.inf), (np.inf, np.inf, np.inf, np.inf, np.inf, np.inf)]

starting_point = [0.606, 2.092 * 10 ** (-3), 0.9 * 10 ** (-3), 2.657 * 10 ** (-10), 8.719 * 10 ** (-11), 0.1]


plot_data(freq, phase, fit_function=phase_to_freq_fit, starting_points=starting_point, bounds=bounds,
          graph_dir_path="./../graphs", experiment_name=experiment_name)

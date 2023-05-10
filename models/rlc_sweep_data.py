from pandas import read_csv
from plotter import plot_data
import numpy as np

# Data Settings
data_path = './../data/rlc_analyzed.csv'
# unpack data
data_frame = read_csv(data_path)

phase = -data_frame["Phase [rad]"]
amplitude = data_frame["Amplitude [V]"]
frequency = data_frame["Frequency [KHz]"]


def phase_to_freq_fit(x, a, b, c):
    return -np.arctan((a * x - 1 / (b * x)) / (1.618)) + c

phase_starting_point = [0.2769, 0.0003, 0]
phase_starting_bounds = ((-100, -np.inf, -np.inf), (np.inf, np.inf, np.inf))

def amp_to_freq_fit(x, a, b, c):
    return 2 / (np.sqrt(
        c ** 2 + (a * x - 1 / (b * x)) ** 2
    ))

amp_starting_point = [0.008, 0.001, 0.8]

plot_data(frequency, phase, phase_to_freq_fit, starting_points=phase_starting_point, bounds=phase_starting_bounds, residuals=True, graph_dir_path="./../graphs", experiment_name="rlc")
plot_data(frequency, amplitude, amp_to_freq_fit, starting_points=amp_starting_point, residuals=True, graph_dir_path="./../graphs", experiment_name="rlc")






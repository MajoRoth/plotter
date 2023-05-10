from pandas import read_csv
from plotter import plot_data

# Data Settings
data_path = './../data/coupled_result.csv'

# unpack data
data_frame = read_csv(data_path)
frequency = data_frame["Frequency [kHz]"]
amplitude = data_frame["Amplitude [V]"]
phase = data_frame["Phase [rad]"]

plot_data(frequency, amplitude, graph_dir_path="./../graphs", experiment_name="coupled rlc")
plot_data(frequency, phase, graph_dir_path="./../graphs", experiment_name="coupled rlc")


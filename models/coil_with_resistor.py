from pandas import read_csv
from plotter import plot_data

# Data Settings
data_path = './../data/coil_with_resistor_22kohm.csv'

# unpack data
data_frame = read_csv(data_path)

phase = data_frame["phase [rad]"]
amplitude = data_frame["amplitude"]
frequency = data_frame["frequency [Hz]"] / 10 ** 3
frequency.name = "frequency [kHz]"

plot_data(frequency, amplitude, graph_dir_path="./../graphs", experiment_name="coil with resistor")

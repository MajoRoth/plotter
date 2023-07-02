from pandas import read_csv
from plotter import plot_data
import numpy as np

# Data Settings
data_path = './../data/d=24.csv'

# preprocess data
data_frame = read_csv(data_path)

filtered_data_frame = data_frame[data_frame["Frequency [Hz]"] >= 1]

a = filtered_data_frame["Amplitude_A [V]"]
freq = filtered_data_frame["Frequency [Hz]"]
freq = freq / 1000
freq.name = "Frequency [kHz]"

experiment_name = None # "coupled_d=0"  # "mutual_inductance"




plot_data(freq, a, graph_dir_path="./../graphs", experiment_name=experiment_name)

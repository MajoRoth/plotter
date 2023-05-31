from pandas import read_csv
from plotter import plot_comparison

# Data Settings
data_path_5 = './../data/d=5.5.csv'
data_path_10 = './../data/d=10.csv'

experiment_name = "compare_distant"

# preprocess data
data_frame_5 = read_csv(data_path_5)
data_frame_10 = read_csv(data_path_10)


a_5 = data_frame_5["Amplitude"]
freq_5 = data_frame_5["Frequency [Hz]"]
freq_5 = freq_5 / 1000
freq_5.name = "Frequency [kHz]"

a_10 = data_frame_10["Amplitude"]
freq_10 = data_frame_10["Frequency [Hz]"]
freq_10 = freq_10 / 1000
freq_10.name = "Frequency [kHz]"



plot_comparison(freq_5, a_5, freq_10, a_10, graph_dir_path="./../graphs", experiment_name=experiment_name)



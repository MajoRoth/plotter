from pandas import read_csv
from plotter import plot_data

# Data Settings
data_path = './../data/rlc_raw.csv'

# preprocess data
data_frame = read_csv(data_path)
data_frame = data_frame.drop(index=0)


time_ms = data_frame["Time"]
amplitude = data_frame["Channel A"]

# process data
time_ms_normal = time_ms.astype(float) + 100
amplitude = amplitude.astype(float)
time_ms_normal.name = "Time [ms]"
amplitude.name = "V_{out} [V]"

plot_data(time_ms_normal, amplitude, None, graph_dir_path="./../graphs", experiment_name="rlc_raw")



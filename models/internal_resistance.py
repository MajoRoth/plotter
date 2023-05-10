from pandas import read_csv
from plotter import plot_data

# Data Settings
data_path = './../data/picoscope_internal_resistance_measurement_1KOhm.csv'

# preprocess data
data_frame = read_csv(data_path)

v_in = data_frame["V_in [V]"]
v_out_milivolt = data_frame["V_out [mV]"]
v_out = v_out_milivolt/1000

v_in.name = "V_{in} [V]"
v_out.name = "V_{out} [V]"

def linear_fit(x, m, b):
     return m*x + b


plot_data(v_in, v_out, linear_fit, graph_dir_path="./../graphs", experiment_name="internal_resistance")



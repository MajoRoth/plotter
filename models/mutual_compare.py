import os
import sys

import numpy as np
from pandas import read_csv
from plotter import plot_data

# Data Settings
data_path = './../data/mutual_big.csv'
CIRCUIT_NAME = "big" # "coil_resistor_47"
# CIRCUIT_NAME = None
# unpack data
data_frame = read_csv(data_path)


amplitude = data_frame["Amplitude"]
amplitude.name = "|H|"
frequency = data_frame["Frequency [Hz]"] / 1000
frequency.name = "frequency [kHz]"
frequency = frequency


plot_data(frequency, amplitude, graph_dir_path="./../graphs", experiment_name=CIRCUIT_NAME)


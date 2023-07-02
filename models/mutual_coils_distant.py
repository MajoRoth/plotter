from pandas import read_csv
from plotter import plot_comparison

distances = [0, 5, 11, 14, 20, 24]

# filtered_data_frame = data_frame[data_frame["Frequency [Hz]"] >= 1]

data_list = [f"./../data/d={d}.csv" for d in distances]
data_frames = [read_csv(path) for path in data_list]
experiment_name = None # "comp"

# columns = [(df["Frequency [Hz]"] / 1000, df["Amplitude"], f"{distances[i]} [cm]") for i, df in enumerate(data_frames)]


columns = list()

for i, df in enumerate(data_frames):
    df = df[df["Frequency [Hz]"] >= 150000]
    df = df[df["Frequency [Hz]"] <= 250000]
    freq = df["Frequency [Hz]"]
    freq.name = "Frequency [kHz]"
    freq = freq / 1000

    amp = df["Amplitude"]

    amp.name = "|H|"
    columns.append((freq, amp, f"{distances[i]} [cm]"))



plot_comparison(columns, graph_dir_path="./../graphs", experiment_name=experiment_name)



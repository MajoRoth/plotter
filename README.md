# Publication Quality Graphs With Python
Creating publication quality graphs with python was never easier!

`plotter.py` allows you to easily create:
- publication quality graphs
- fitting any function
- create residuals


## Installation
Just clone the git repository or download `plotter.py`.

you can find in the repository examples for experiments i preformed and created graphs for the results.

## Create Beautiful Graphs
Import the libraries
```python
from pandas import read_csv
from plotter import plot_data
import numpy as np
```

Extract your data from the csv using pandas. 

```python
data_path = './../data/rlc_analyzed.csv'
data_frame = read_csv(data_path)
phase = data_frame["Phase [rad]"]
frequency = data_frame["Frequency [KHz]"]
```
Note that `plotter.py` uses the name of the columns for the titles of the graph. If you not happy with the column namings,
change it in the `.csv` or change it using pandas `phase.name = new_name`.

Choose your fit function and define starting point and bounds if needed.
```python
def phase_to_freq_fit(x, a, b, c):
    return -np.arctan((a * x - 1 / (b * x)) / (1.618)) + c

phase_starting_point = [0.2769, 0.0003, 0]
phase_bounds = ((-100, -np.inf, -np.inf), (np.inf, np.inf, np.inf))
```

Now you can use `plot_data` to get the desired graph
```python
plot_data(frequency, phase, phase_to_freq_fit, starting_points=phase_starting_point, bounds=phase_starting_bounds, residuals=True, save=False)
```
The fitting parameters will be printed with std values

| parameter |   value   |    std    |
|:---------:|:---------:|:---------:|
|     a     |  0.0271   | 0.000144  |
|     b     | 0.0003524 | 1.866e-06 |
|     c     |  -0.1745  | 0.003361  |

and you will get the following graph

![alt text](https://github.com/MajoRoth/rlc_lab/blob/main/graphs/graph%3A%20Phase%20%5Brad%5D%20as%20function%20of%20Frequency%20%5BKHz%5D.png "Graph")

## `plot_data` Parameters
- x_data
- y_data
- fit_function
- starting_points
- bounds
- residuals
- save





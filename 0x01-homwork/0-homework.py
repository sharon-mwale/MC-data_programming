import matplotlib.pyplot as mlt
import numpy as nmpi

x_values = nmpi.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
y_values = nmpi.array([35000, 42000, 38000, 41000, 38000, 39000, 45000, 47000, 43000, 42000, 48000, 51000])

mlt.bar(x_values, y_values)

mlt.xlabel("Months")
mlt.ylabel("Sales amount")

mlt.show()
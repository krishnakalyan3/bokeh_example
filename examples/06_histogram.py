#!/usr/bin/env python3

from bokeh.plotting import figure, output_file, show

# prepare some data
x = [0.1, 0.3, 0.5, 0.1]

# output to static HTML file
output_file("../plots/06_line_plot.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example")

# add a line renderer with legend and line thickness
p.hbar(x, legend="Sample", line_width=2, right=[1, 2 ,3, 4], left=0, height=0.5)

# show the results
show(p)
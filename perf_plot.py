#!/usr/bin/env python3
from bokeh.plotting import figure
from bokeh.charts import Bar, output_file, show


def plot(x_data, y_data):
    plt = figure(x_range=x_data, title='Algorithm Performance Chart', x_axis_label='Release Version',
               y_axis_label='Time Taken (in seconds)')

    plt.circle(x=x_data, y=y_data, color='#F0027F', size=5)
    plt.line(x=x_data, y=y_data, line_width=1, line_dash='dashed')
    return plt

if __name__ == "__main__":
    x = ['tag_1', 'tag_2', 'tag_3']
    y = [1.5, 2, 1.7]
    p = plot(x, y)
    show(p)
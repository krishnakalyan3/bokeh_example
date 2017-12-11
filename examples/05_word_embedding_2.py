#!/usr/bin/env python3

from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool
from bokeh.models import ColumnDataSource, LabelSet

output_file("toolbar.html")

source = ColumnDataSource(data=dict(
    x=[1, 2, 3, 4, 5],
    y=[2, 5, 8, 2, 7],
    desc=['A', 'b', 'C', 'd', 'E'],
))

hover = HoverTool(tooltips=[
    ("index", "$index"),
    ("(x,y)", "($x, $y)"),
    ("desc", "@desc"),
])



p = figure(tools=[hover],
           title="Mouse over the dots")

p.circle('x', 'y', source=source)
labels = LabelSet(x='x', y='y', text='desc', y_offset=0,
                    text_color="red",
                    text_align='center',
                    source=source, render_mode='canvas')

p.add_layout(labels)
show(p)

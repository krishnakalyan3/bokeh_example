#!/usr/bin/env python3

from bokeh.models import ColumnDataSource, LabelSet
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool
import numpy as np
import pandas as pd

TITLE = "Awesome Title"
TITLE_FONT = '30pt'
X_LAB = 'x'
Y_LAB = 'y'
PLT_WIDTH = 1200

TOOLS = "hover,reset,save,pan"

df = pd.DataFrame(
    {
        "x": np.array(range(5)),
        "y": np.array(range(10, 15)),
        "cat": ['a1', 'b1', 'c1', 'd1', 'e1']
    }
)

colors = ["red", "olive", "darkred", "goldenrod", "skyblue"]

# output to static HTML file
output_file("../plots/02_word_embedding_plot.html")


hover = HoverTool(
        tooltips=[

            ("(x,y)", "($x, $y)"),
            ("cat", "@cat")
        ]
    )

p = figure(tools=[hover], plot_width=PLT_WIDTH,
           x_axis_label=X_LAB, y_axis_label=Y_LAB,
           title=TITLE)

p.title.text_font_size = TITLE_FONT

p.scatter(x=df['x'], y=df['y'], color=colors)

labels = LabelSet(x='x', y='y', text='cat', y_offset=0,
                  text_font_size="20pt", text_color="red",
                  text_align='center',
                  source=ColumnDataSource(df), render_mode='canvas')

p.add_layout(labels)




show(p)

# TO DO
# Add custom color to each point
# Change label size based on some number
# Add hoverplot
    # Count
    # Name of the Label
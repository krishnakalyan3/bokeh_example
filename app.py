#!/usr/bin/env python3

from flask import Flask, render_template
from flask_cors import CORS
from perf_plot import plot
from bokeh.embed import components

app = Flask(__name__)
CORS(app)


@app.route("/")
def chart():
    x = ['1.0', '2.7', '3.0']
    y = [1.5, 2, 1.7]
    plt = plot(x, y, title="")
    script, div = components(plt)
    return render_template("chart.html",  script=script, div=div)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)

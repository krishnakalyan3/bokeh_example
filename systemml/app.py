#!/usr/bin/env python3

from flask import Flask, render_template
from flask_cors import CORS
from perf_plot import plot
from bokeh.embed import components
from flask import Flask, flash, redirect, render_template, \
     request, url_for
from conn_test import init_connection, get_backends, get_algos, get_release_time

app = Flask(__name__)
CORS(app)


@app.route("/")
def chart():
    backends_sel = request.args.get('backend', default='singlenode')
    algos_sel = request.args.get('algo', default='total_time')

    psql_conn = init_connection()
    backends = get_backends(psql_conn)
    algos = get_algos(psql_conn)
    x, y = get_release_time(psql_conn, backends_sel, algos_sel)
    print(x)
    plt = plot(x, y, title="")
    script1, div1 = components(plt)
    return render_template("child.html",  script1=script1, div1=div1,
                           backend_type=backends,
                           algo_type=algos)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)

#!/usr/bin/env python3

from flask import Flask, render_template
from flask_cors import CORS
from perf_plot import plot
from bokeh.embed import components
from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = Flask(__name__)
CORS(app)


@app.route("/")
def chart():
    warm_text = request.args.get('backend')
    print(warm_text)
    x = ['1.0', '2.7', '3.0']
    y = [1.5, 2, 1.7]
    plt = plot(x, y, title="")
    script1, div1 = components(plt)
    return render_template("child.html",  script1=script1, div1=div1,
                           backend_type=[{'name':'spark_hybrid'}, {'name':'singlenode'}],
                           algo_type= [{'name':'multinomial_data-gen_none_dense_10k_100'},
                                       {'name':'multinomial_data-gen_none_sparse_10k_100'}])
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)

from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os
import joblib
from sklearn.metrics import adjusted_mutual_info_score
from IPython.display import HTML
import pickle

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, render_template, jsonify  # Import jsonify
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

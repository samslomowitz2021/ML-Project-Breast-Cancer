from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
from modelHelper import ModelHelper
import numpy as np
import os


#init app and class
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
modelHelper = ModelHelper()

# from modelHelper import ModelHelper
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/about")
def aboutme():
    # Return template and data
    return render_template("about.html")

@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableau.html")

@app.route("/table")
def table():
    # Return template and data
    return render_template("table.html")

@app.route("/sources")
def sources():
    # Return template and data
    return render_template("workCited.html")

@app.route("/prediction")
def prediction():
    # Return template and data
    return render_template("prediction.html")

# POST REQUEST LISTENER
@app.route("/makePredictions", methods=["POST"])
def makePrediction():
    content = request.json["data"]
    print(content)
    
  
    
    # parse

    # parse
    concave_points_worst_bins = content["concave_points_worst_bins"]
    perimeter_worst_bins = content["perimeter_worst_bins"]
    concave_points_mean_bins = content["concave_points_mean_bins"]
    radius_worst_bins = content["radius_worst_bins"]
    
    prediction = modelHelper.makePredictions(concave_points_worst_bins, perimeter_worst_bins,
        concave_points_mean_bins, radius_worst_bins)
    print(prediction)

    return(jsonify({"ok": True, "prediction": str(prediction)}))
    




#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)

# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request, url_for
from datetime import datetime
from model import determine_air_quality
import os
# -- Initialization section --
app = Flask(__name__)
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())
@app.route('/AirPollution')
def AirPollution():
    return render_template("AirPollution.html", time = datetime.now())
@app.route('/WaterPollution')
def WaterPollution():
    return render_template("WaterPollution.html", time = datetime.now())
@app.route('/LandPollution')
def LandPollution():
    return render_template("LandPollution.html", time = datetime.now())
@app.route('/WaysToHelp')
def WaysToHelp():
    return render_template("WaysToHelp.html", time = datetime.now())
@app.route('/Survey')
def Survey():
    return render_template("Survey.html", time = datetime.now())
@app.route("/SurveyResults", methods = ["GET", "POST"])
def getSurveyResults():     
    postal = request.form["postal"]
    country = request.form["country"]
    air_quality = determine_air_quality(postal, country)
    return render_template("SurveyResults.html", time = datetime.now(), airquality = air_quality)
    
#user_borough = request.form["borough"]

#air_quality = determine_air_quality(user_borough)

#return render_template("SurveyResults.html", time = datetime.now(), airquality = air_quality)
    
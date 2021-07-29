# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request, url_for
from datetime import datetime
from model import determine_air_quality
from model import recycle
from model import reusableProducts
from model import dietType
from model import transportation
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
    recycleFreq = request.form["recycleFreq"]
    reusable = request.form["reusable"]
    diet = request.form["diet"]
    trans = request.form["trans"]
    
    postal = request.form["postal"]
    country = request.form["country"]

    rec = recycle(recycleFreq)
    rp = reusableProducts(reusable)
    dt = dietType(diet)
    tt = transportation(trans)

    air_quality = determine_air_quality(postal, country)
    return render_template("SurveyResults.html", time = datetime.now(), airquality = air_quality, rec = rec, rp = rp, dt = dt, tt = tt)
    
#user_borough = request.form["borough"]

#air_quality = determine_air_quality(user_borough)

#return render_template("SurveyResults.html", time = datetime.now(), airquality = air_quality)
    
from numpy import save
from flask import Flask, render_template, request, redirect, send_file
from merge import start_scrapping
from exporter import save_to_file

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs: 
            jobs = existingJobs
        else:
            jobs = start_scrapping(word)
            db[word] = jobs
        return render_template("report.html", searchingBy = word, resultsNum = len(jobs), jobs = jobs)
    else:
        return redirect("/")

@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word) 
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")

    
app.run(host="0.0.0.0")
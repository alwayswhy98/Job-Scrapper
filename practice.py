from flask import Flask, render_template, request, redirect
from main import start_scrapping

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

app.run(host="0.0.0.0")
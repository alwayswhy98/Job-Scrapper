from flask import Flask, render_template, request, redirect

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        return render_template("report.html", searchingBy = word)
    else:
        return redirect("/")

app.run(host="0.0.0.0")
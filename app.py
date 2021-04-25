"""Entrypoint for flask application with kio tasks."""

from flask import Flask, render_template
import os
import subprocess


app = Flask(__name__)


# TODO: add icons for all task buttons
# TODO: add login system
# TODO: add statistic
# TODO: add 2005 y. tas

@app.route("/")
@app.route("/index")
def index():
    """Render main page information."""
    user = {"nickname": "Dear User"}  # выдуманный пользователь
    return render_template(
        "index.html",
        title="Home",
        user=user,
    )


@app.route("/start_task_ru/<name>")
def start_task_ru(name):
    """Start task from KIO_competition."""
    fnull = open(os.devnull, "w")
    args = "static\\flash.exe static\\KIO_competition\\KIO_ru_20" + name
    subprocess.call(args, stdout=fnull, stderr=fnull, shell=False)


@app.route("/start_task_en/<name>")
def start_task_en(name):
    """Start task from KIO_competition_en."""
    fnull = open(os.devnull, "w")
    args = "static\\flash.exe static\\EN_tasks\\" \
           "KIO_competition_en\\KIO_en_20" + name
    subprocess.call(args, stdout=fnull, stderr=fnull, shell=False)


@app.route("/start_kio_school_task/<name>")
def start_kio_school_task(name):
    """Start task from KIO_SCHOOL"""
    fnull = open(os.devnull, "w")
    args = "static\\flash.exe static\\KIO_SCHOOL\\" + name
    subprocess.call(args, stdout=fnull, stderr=fnull, shell=False)


@app.route("/go_back")
def go_back():
    """Return to previous page."""
    return "<script>history.go(-1)</script>"


@app.route("/current_competition")
def open_page():
    """Open current competition page."""
    return render_template("current_competition.html")


@app.route("/english_tasks")
def open_en_tasks():
    """Open english tasks page."""
    return render_template("english_tasks.html")


@app.route("/english_page")
def open_en_page():
    """Open page for all english tasks."""
    return render_template("english_page.html")


@app.route("/old_files")
def old_files():
    """Open old files. This function has no use in current moment."""
    return render_template("old_files.html")


@app.route("/kio_school_files")
def kio_school_files():
    """Open KIO School page."""
    return render_template("kio_school_files.html")


@app.route("/standalone_ru_tasks")
def standalone_ru_tasks():
    """Open standalone ru tasks page."""
    return render_template("standalone_RU_tasks.html")


@app.route("/start_2006_8_task/<year>/<name>")
def start_2006_8_task(name, year):
    """Start task Zanimatelnie zadachi"""
    fnull = open(os.devnull, "w")
    if year == "zadachi":
        args = "static\\Standalone_RU_tasks\\zanimatelnie_zadachi\\math.exe"
    else:
        args = "static\\Standalone_RU_tasks\\KIO20" + year \
               + name + "\\KIO20" + year + name + ".exe"
    subprocess.call(args, stdout=fnull, stderr=fnull, shell=False)


if __name__ == "__main__":
    app.run(debug=True)

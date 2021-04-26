"""Entrypoint for flask application with kio tasks."""

import subprocess

from flask import Flask, render_template

app = Flask(__name__)


# TODO: add icons for all task buttons
# TODO: add login system
# TODO: add statistic
# TODO: add 2005 y. tas
# TODO: universal functions for page opening
# TODO: open tasks on the top

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


@app.route("/<category>")
def open_any_task(category):
    """Open."""
    return render_template(f"{category}.html")


@app.route("/start_task_ru/<name>")
def start_task_ru(name):
    """Start task from KIO_competition."""
    args = "static\\flash.exe static\\KIO_competition\\KIO_ru_20" + name
    subprocess.call(args)
    return ""


@app.route("/start_task_en/<name>")
def start_task_en(name):
    """Start task from KIO_competition_en."""
    args = "static\\flash.exe static\\EN_tasks\\" \
           "KIO_competition_en\\KIO_en_20" + name
    subprocess.call(args)
    return ""


@app.route("/start_kio_school_task/<name>")
def start_kio_school_task(name):
    """Start task from KIO_SCHOOL"""
    args = "static\\flash.exe static\\KIO_SCHOOL\\" + name
    subprocess.call(args)
    return ""


@app.route("/start_2006_8_task/<year>/<name>")
def start_2006_8_task(name, year):
    """Start task Zanimatelnie zadachi."""
    if year == "zadachi":
        args = "static\\Standalone_RU_tasks\\zanimatelnie_zadachi\\math.exe"
    else:
        args = "static\\Standalone_RU_tasks\\KIO20" + year \
               + name + "\\KIO20" + year + name + ".exe"
    subprocess.call(args)
    return ""


if __name__ == "__main__":
    app.run(debug=True)

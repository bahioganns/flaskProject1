from flask import Flask, render_template
import os
import subprocess

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Dear User'}  # выдуманный пользователь
    return render_template('index.html',
                           title='Home',
                           user=user)


@app.route('/start_task_ru/<name>')
def start_task_ru(name):
    FNULL = open(os.devnull, 'w')
    args = "static\\flash.exe static\\KIO_competition\\KIO_ru_20" + name
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)


@app.route('/start_task_en/<name>')
def start_task_en(name):
    FNULL = open(os.devnull, 'w')
    args = "static\\flash.exe static\\EN_tasks\\KIO_competition_en\\KIO_en_20" + name
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)


@app.route('/start_kio_school_task/<name>')
def start_kio_school_task(name):
    FNULL = open(os.devnull, 'w')
    args = "static\\flash.exe static\\KIO_SCHOOL\\" + name
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)



@app.route("/go_back")
def go_back():
    return "<script>history.go(-1)</script>"


@app.route("/current_competition")
def open_page():
    return render_template("current_competition.html")


@app.route('/english_tasks')
def open_en_tasks():
    return render_template("english_tasks.html")


@app.route('/english_page')
def open_en_page():
    return render_template("english_page.html")


@app.route("/old_files")
def old_files():
    return render_template("old_files.html")


@app.route("/kio_school_files")
def kio_school_files():
    return render_template("kio_school_files.html")



@app.route("/standalone_ru_tasks")
def standalone_ru_tasks():
    return render_template("standalone_RU_tasks.html")


@app.route('/start_2006_8_task/<year>/<name>')
def start_2006_8_task(name, year):
    FNULL = open(os.devnull, 'w')
    if year == "zadachi":
        args = "static\\Standalone_RU_tasks\\zanimatelnie_zadachi\\math.exe"
    else:
        args = "static\\Standalone_RU_tasks\\KIO20" + year + name + "\\KIO20" + year + name + ".exe"
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)


if __name__ == '__main__':
    app.run(debug=True)

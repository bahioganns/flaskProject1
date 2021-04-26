"""Entrypoint for flask application with kio tasks."""

import subprocess  # noqa: S404

from flask import Flask, render_template

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


@app.route("/<category>")
def open_any_task(category):
    """Open any html page from template directory."""
    if category == "favicon.ico":
        return ""
    return render_template(f"{category}.html")


@app.route("/<category>/<name>/", defaults={"year": None})
@app.route("/<category>/<year>/<name>")
def start_task(category, name, year):
    """Start any task."""
    subprocess.call(  # noqa: S603
        get_path(category, name, year),
        stdout=subprocess.DEVNULL,
    )
    return ""


def get_path(category, name, year):
    """Return path to the task."""
    task_path = None

    if category == "start_2006_8_task":
        if year == "zadachi":
            task_path = "Standalone_RU_tasks/zanimatelnie_zadachi/math.exe"
        else:
            kio_name = f"KIO20{year}{name}"
            task_path = f"Standalone_RU_tasks/{kio_name}/{kio_name}.exe"

    elif category == "start_kio_school_task":
        task_path = f"flash.exe static/KIO_SCHOOL/{name}"

    elif category == "start_task_en":
        task_path = (
            f"flash.exe static/EN_tasks/KIO_competition_en/KIO_en_20{name}"
        )

    elif category == "start_task_ru":
        task_path = f"flash.exe static/KIO_competition/KIO_ru_20{name}"

    return f"static/{task_path}"


if __name__ == "__main__":
    app.run(debug=True)  # noqa: S201

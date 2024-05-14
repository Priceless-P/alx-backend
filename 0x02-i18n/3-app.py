#!/usr/bin/env flask
"""Parametrize templates"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


def get_locale():
    """Get user locale"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@app.route('/')
def index():
    """Returns 3-index.html"""
    home_title = gettext("Welcome to Holberton")
    home_header = gettext("Hello world")

    return render_template("3-index.html", strict_slashes=False,
                            home_header=home_header, home_title=home_title)


if __name__ == "__main__":
    app.run()

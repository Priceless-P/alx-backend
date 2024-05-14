#!/usr/bin/env flask
"""Get locale from request"""
from flask import Flask, render_template, request
from flask_babel import Babel


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
    """Returns 2-index.html"""
    return render_template("2-index.html", strict_slashes=False)


if __name__ == "__main__":
    app.run()

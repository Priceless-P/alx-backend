#!/usr/bin/env flask
"""Basic Babel Setup"""
from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

@app.route('/')
def index():
    """Returns 1-index.html"""
    return render_template("1-index.html", strict_slashes=False)


if __name__ == "__main__":
    app.run()

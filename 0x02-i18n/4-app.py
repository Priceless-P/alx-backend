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
app.config.from_object(Config)


def get_locale():
    """Get user locale"""
    locale = request.args.get("locale", "").strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])

babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def index():
    """Returns 4-index.html"""
    home_title = gettext("Welcome to Holberton")
    home_header = gettext("Hello world")

    return render_template("4-index.html", strict_slashes=False,
                            home_title=home_title,
                            home_header=home_header)


if __name__ == "__main__":
    app.run()

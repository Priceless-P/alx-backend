#!/usr/bin/env flask
"""Parametrize templates"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user(id):
    """Returns a user dictionary if a user ID exists"""
    return users.get(int(id), 0)


@app.before_request
def before_request():
    """Executed before any other function"""
    id = request.args.get('login_as', 0)
    user = get_user(id)
    setattr(g, 'user', user)
    print(g.user.name)


@app.route('/')
def index():
    """Returns 4-index.html"""
    home_title = gettext("Welcome to Holberton")
    home_header = gettext("Hello world")

    return render_template("5-index.html", strict_slashes=False,
                           home_title=home_title,
                           home_header=home_header)


if __name__ == "__main__":
    app.run()

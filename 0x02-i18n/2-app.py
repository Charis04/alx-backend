#!/usr/bin/env python3
"""
A basic flask app with basic babel set up
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Config class for intiating babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Function that determines the best language for user"""
    return request.accept_languages.best_match(app.config['Languages'])


@app.route('/')
def home():
    """Route to homepage"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)

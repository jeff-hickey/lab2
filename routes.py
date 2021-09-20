from flask import Flask, render_template, request

import joblib

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def hello():
    return f'hello world {person}'


if __name__ == '__main__':
    app.run(debug=True)


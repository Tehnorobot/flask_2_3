from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm


app = Flask(__name__)

@app.route('/list_prof/<param>')
def index(param):
    return render_template('list_val.html', param=param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
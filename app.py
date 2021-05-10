from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import os
import numpy as np

app = Flask(__name__)

######## Flask class HelloForm(Form):
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')


if __name__ == '__main__':
    app.run(debug=True)
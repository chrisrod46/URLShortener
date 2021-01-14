#!/usr/bin/env python3
#
# Christopher Rodriguez
# CPSC 223p-03
# 2020-11-17
# chrisrod46@csu.fullerton.edu
#
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/<name>', methods=['GET','POST'])
@app.route('/', methods=['GET','POST'])
def hello_world(name='World'):

    if request.method == 'POST':
        return render_template('home.html', templatename = request.form['name'])

    return render_template('home.html', templatename=name)

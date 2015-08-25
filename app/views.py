from flask import render_template, request, send_from_directory
from flask.ext.bower import Bower
from app import app
import RPi.GPIO as IO

IO.setmode(IO.BCM)
s1 = 19
IO.setup(s1, IO.OUT)
s2 = 13
IO.setup(s2, IO.OUT)
m1 = 6
IO.setup(m1, IO.OUT)
m2 = 26
IO.setup(m2, IO.OUT)

def switch_engines(sp1, sp2, mo1, mo2):
    IO.output(s1, sp1)
    IO.output(s2, sp2)
    IO.output(m1, mo1)
    IO.output(m2, mo2)

switch_engines(0, 0, 0, 0)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/engines/<command>')
def engines_support(command):
    if command == 'forward':
        switch_engines(1, 1, 0, 0)
    elif command == 'left':
        switch_engines(1, 1, 0, 1)
    elif command == 'right':
        switch_engines(1, 1, 1, 0)
    elif command == 'back':
        switch_engines(1, 1, 1, 1)
    else:
        switch_engines(0, 0, 0, 0)
    return '{}'

Bower(app)

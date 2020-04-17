from flask import Flask, render_template, flash
from flask_script import Manager
from flask_moment import Moment
from flask_bootstrap import Bootstrap


from app import views
from app import config
from app import logics
from app import forms

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#from datetime import datetime
import timeit
import time
import io
import base64

app = Flask(__name__)
#from app import logging

from app.cube2 import Cube


app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

manager = Manager(app)
moment = Moment(app)


from flask import Flask, render_template, flash
from flask_script import Manager
from flask_moment import Moment
from flask_bootstrap import Bootstrap


import views
import config
#import logics
#import forms

"""import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt"""


app = Flask(__name__)


#from app.cube2 import Cube

"""PORT = int(env.get("PORT", 9082))
DEBUG_MODE = int(env.get("DEBUG_MODE", 1))

#Gunicorn config
bind = ":" + str(PORT)"""

app['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

manager = Manager(app)
moment = Moment(app)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
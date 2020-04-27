from flask import Flask #, render_template, flash
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_moment import Moment

"""import numpy as np
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt


from datetime import datetime
import time"""



import config
import forms
import logics
from views import  *


import io
import base64

#import cube2
from cube2 import Cube

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

manager = Manager(app)
moment = Moment(app)










if __name__ == '__main__':
	app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
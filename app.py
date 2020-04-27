from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_moment import Moment

import numpy as np
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt


from datetime import datetime
import time



import config
import forms
import logics


import io
import base64

#import cube2
from cube2 import Cube

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

manager = Manager(app)
moment = Moment(app)



from views import  *




@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html', current_time=datetime.utcnow()), 500


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html', current_time=datetime.utcnow()), 404

@app.errorhandler(MemoryError)
def out_of_memory(e):
        return render_template('memeoryerror.html', current_time=datetime.utcnow()), 404

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
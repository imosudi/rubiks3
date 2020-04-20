import os
import sys

from flask import Flask, render_template, flash
"""from flask_script import Manager
from flask_moment import Moment
from flask_bootstrap import Bootstrap"""


app = Flask(__name__)




"""app['SECRET_KEY'] = 'hard to guess string'"""

bootstrap = Bootstrap(app)

manager = Manager(app)
moment = Moment(app)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
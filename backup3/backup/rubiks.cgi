#!/usr/bin/python

from wsgiref.handlers import CGIHandler
#from myapp import app
from rubiks import *


CGIHandler().run(app)

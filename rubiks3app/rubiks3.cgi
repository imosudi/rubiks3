#!/usr/bin/python

from wsgiref.handlers import CGIHandler
#from myapp import app
from rubiks3app import *


CGIHandler().run(app)
#config.py
import os
import sys
#sys.path.insert(0, "../venv/lib/python3.6/site-packages")
#Dockerfile COPY --from=builder /app/build "../venv/lib/python3.6/site-packages"
sys.path.insert(0, "../python3.6/site-packages")

from os import environ as env
#Importing Logging
#import logging
import os.path
#import multiprocessing



import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#from datetime import datetime
import timeit
import time
import io
import base64



PORT = int(env.get("PORT", 9082))
DEBUG_MODE = int(env.get("DEBUG_MODE", 1))

#Gunicorn config
bind = ":" + str(PORT)
#workers = multiprocessing.cpu_count() * 2 + 1
#threads = 2 * multiprocessing.cpu_count()

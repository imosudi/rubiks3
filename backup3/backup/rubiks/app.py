#docker build -t imosudi/rubiks3ubuntufs:v12 . && docker run -p 9082:9082 imosudi/rubiks3ubuntufs:v12
from flask import Flask, render_template, flash
from flask_script import Manager
from flask_moment import Moment
from flask_bootstrap import Bootstrap


from datetime import datetime
import timeit
import time


import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


from sys import getsizeof


import io
import base64

# Custom llbrary addition
import config
import logics
import forms

#import cube2
from cube2 import Cube

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

manager = Manager(app)
moment = Moment(app)



@app.route('/', methods = ['GET', 'POST'])
def index():
    #start = timeit.timeit()
    #print('plot_url size before None', getsizeof(plot_url))
    #plot_url = None
    #fig = None
    #img = None
    #print('plot_url size after None', getsizeof(plot_url))
    #print('for num at load or reload the fig size is ', getsizeof(fig), 'img size', getsizeof(img), 'plot_url size', getsizeof(plot_url))
    start = time.time()
    form = forms.rubikForm()
    formM = forms.rubikFormM()
    rubikOp = logics.rubikOperation()
    num = rubikOp.inputNbyNbyN()
    #print(type(num))
    if num is None:
        flash('')
        num = 3
        cubeletSum = 27 
        FacesCubelets = 26
        hidden = 1
        m = 1
        formM.m.data = m

    elif num > 1 and num < 25:
        cubeletSum = rubikOp.numCubelets()
        FacesCubelets = rubikOp.numFacesCubelets()
        hidden = rubikOp.hiddenCubelets()
        m = rubikOp.nM()
        formM.m.data  = m
    
    elif num < 2:
        flash ('Provide n (1<n<14) ')
        num = 3
        cubeletSum = 27
        FacesCubelets = 26
        hidden = 1
        m = 1
        formM.m.data = m 
    
    elif num > 24:
        flash ('Provide n (1<n<14) TOO MUCH')
        num = 3
        cubeletSum = 27 
        FacesCubelets = 26 
        hidden = 1 
        m = 1 
        formM.m.data  = m

    img = io.BytesIO()
    #np.random.seed(42)
    fig = Cube(num, whiteplastic=True)
    fig.render(flat=False,  views=True).savefig(img, format='png',  dpi=965 )

    #matplotlib.pyplot.close(fig)


    #print('for', num, 'the fig size is ', getsizeof(fig), 'img size', getsizeof(img), 'plot_url size', getsizeof(plot_url))
    img.seek(0)
    #print('img size', getsizeof(img))
    plot_url = base64.b64encode(img.getvalue()).decode()
    fig = None
    #img = io.BytesIO()
    #img = None
    #plt.clf()
    plt.close()

    #delay = timeit.timeit()
    end = time.time()
    delay = end - start

    timer=time.time()


    #print(img)
    #print('img type is', type(img))

    #print('fig type is', type(fig))
    #plot_url = 0
    #print('for', num, 'the fig size is ', getsizeof(fig), 'img size', getsizeof(img), 'plot_url size', getsizeof(plot_url))

    """if form.validate() :
        return render_template('index.html', plot_url=plot_url, delay=delay, time=time, timer=timer,
                FacesCubelets=FacesCubelets, hidden=hidden, m=m, cubeletSum=cubeletSum,
                form=form, formM=formM, num=num, current_time=datetime.utcnow())
        img = io.BytesIO()
        plot_url = None
    else:
        return render_template('index.html', plot_url=plot_url, delay=delay, time=time, timer=timer,
                FacesCubelets=FacesCubelets, hidden=hidden, m=m, cubeletSum=cubeletSum,
                form=form, formM=formM, num=3, current_time=datetime.utcnow())"""

    return render_template('index.html', plot_url=plot_url, delay=delay, time=time, timer=timer, 
    FacesCubelets=FacesCubelets, hidden=hidden, m=m, cubeletSum=cubeletSum, 
    form=form, formM=formM, num=num, current_time=datetime.utcnow())

    """print(img)
    print(fig)
    
    print(type(img))
    print(type(fig))"""

    #fig.clear()
    #img = io.BytesIO()

    #print(img)
    #print(fig)

    """else:
        return render_template('index.html', plot_url=plot_url, delay=delay, time=time, timer=timer,
                FacesCubelets=FacesCubelets, hidden=hidden, m=m, cubeletSum=cubeletSum,
                form=form, formM=formM, num=3, current_time=datetime.utcnow())"""

    pass


@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html', current_time=datetime.utcnow()), 500


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html', current_time=datetime.utcnow()), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)

""" https://stackoverflow.com/questions/26088946/string-bytes-issue-when-upgrading-from-python2-to-python3"""
"""if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    #manager.run()"""
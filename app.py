from flask import Flask, render_template, flash
from flask_script import Manager
from flask_moment import Moment
from flask_bootstrap import Bootstrap


from datetime import datetime


# Custom llbrary addition
import config
import logics
import forms
#import routes

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

manager = Manager(app)
moment = Moment(app)



@app.route('/', methods = ['GET', 'POST'])
def index():
    #return "<h1> Hello World from FUT Minna"
    form = forms.rubikForm()
    formM = forms.rubikFormM()
    rubikOp = logics.rubikOperation()
    num = rubikOp.inputNbyNbyN()
    print(type(num))
    if num is None:
        flash('')
        num = 3
        cubeletSum = 27 
        FacesCubelets = 26
        hidden = 1
        m = 1

    elif num > 1 and num < 15:
        cubeletSum = rubikOp.numCubelets()
        FacesCubelets = rubikOp.numFacesCubelets()
        hidden = rubikOp.hiddenCubelets()
        m = rubikOp.nM()
        formM.m.data  = m
    elif num > 14:
        flash ('Provide n (1<n<14) TOO MUCH')
        num = 3
        cubeletSum = 27 
        FacesCubelets = 26 
        hidden = 1 
        m = 1 
        formM.m.data  = m
    return render_template('index.html',
    FacesCubelets=FacesCubelets, hidden=hidden, m=m, cubeletSum=cubeletSum, 
    form=form, formM=formM, num=num, current_time=datetime.utcnow())
    pass


@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html', current_time=datetime.utcnow()), 500


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html', current_time=datetime.utcnow()), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)


"""if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    #manager.run()"""

    




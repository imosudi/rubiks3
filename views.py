from flask import Flask, render_template


from datetime import datetime
import time


from app import app

@app.route('/', methods = ['GET', 'POST'])
def index():
    pageName = "home"
    #start = timeit.timeit()
    #print('plot_url size before None', getsizeof(plot_url))
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
        flash ('Provide n (1<n<25) ')
        num = 3
        cubeletSum = 27
        FacesCubelets = 26
        hidden = 1
        m = 1
        formM.m.data = m 
    
    elif num > 24:
        flash ('Provide n (1<n<25) TOO MUCH')
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


    img.seek(0)
    #print('img size', getsizeof(img))
    plot_url = base64.b64encode(img.getvalue()).decode()
    fig = None

    plt.close()

    #delay = timeit.timeit()
    end = time.time()
    delay = end - start

    timer=time.time()


    return render_template('index.html', plot_url=plot_url, delay=delay, time=time, timer=timer, 
    FacesCubelets=FacesCubelets, hidden=hidden, m=m, cubeletSum=cubeletSum, pageName = pageName,  
    form=form, formM=formM, num=num, current_time=datetime.utcnow())


    pass



@app.route('/another', methods = ['GET'])
def another():
    pageName = "another"
    return render_template('about.html', pageName = pageName,  current_time=datetime.utcnow())

@app.route('/contact', methods = ['GET'] )
def contact():
    pageName = "contact"
    return render_template('contact.html',  pageName = pageName, current_time=datetime.utcnow())

@app.route('/about', methods = ['GET'])
def about():
    pageName = "about"
    return render_template('about.html', pageName = pageName,  current_time=datetime.utcnow())


from flask import Flask


import config


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

manager = Manager(app)
moment = Moment(app)


@app.route('/')
def hello_world():
	return 'Hello, World!'


@app.route('/about', methods = ['GET'])
def about():
    pageName = "about"
    return render_template('about.html', pageName = pageName,  current_time=datetime.utcnow())

@app.route('/contact', methods = ['GET'] )
def contact():
    pageName = "contact"
    return render_template('contact.html',  pageName = pageName, current_time=datetime.utcnow())


    


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
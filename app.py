from flask import Flask, render_template
from flask_script import Manager
from flask_moment import Moment
from flask_bootstrap import Bootstrap


from datetime import datetime


#addition
import config
#import routes

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

manager = Manager(app)
moment = Moment(app)



@app.route('/', methods = ['GET', 'POST'])
def index():
    #return "<h1> Hello World from FUT Minna"
    return render_template('index_1.html', 
		current_time=datetime.utcnow())#
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

from flask import Flask, render_template
from flask_script import Manager
from flask_moment import Moment
from flask_bootstrap import Bootstrap


from datetime import datetime


#addition
import config
import routes

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

manager = Manager(app)
moment = Moment(app)



@app.route('/', methods = ['GET', 'POST'])
def index():
    #return "<h1> Hello World from FUT Minna"
    return render_template('index.html', 
		current_time=datetime.utcnow())#
    pass







if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)




"""if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    #manager.run()"""

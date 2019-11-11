from flask import Flask, render_template
from flask_script import Manager
from flask_moment import Moment



from datetime import datetime


#addition
import config


app = Flask(__name__)




@app.route('/')
def index():
    return "<h1> Hello World from FUT Minna"
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

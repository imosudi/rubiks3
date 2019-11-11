from flask import Flask
import config



app = Flask(__name__)




@app.route('/')
def index():
    return "<h1> Hello World from FUT Minna"
    pass



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)




"""if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    #manager.run()"""

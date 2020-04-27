from flask import Flask, render_template


from datetime import datetime
import time


from app import app




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


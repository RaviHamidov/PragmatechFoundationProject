from app import app
from flask import render_template,request,redirect

@app.route('/')
def index():
    return render_template('app/index.html')
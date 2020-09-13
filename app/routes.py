from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    # return "Hello, World!"
    return render_template('index.html', my_string="WHEEEEEEEE", my_list=[0,1,2,3,4,5])

@app.route('/bec')
def bec():
    return "I ❤️ Bec"


from app import app
from flask import render_template

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/favorite5')
def favorite_five():
    return render_template('favorite5.html')
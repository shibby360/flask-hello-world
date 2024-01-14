from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'About'
    
@app.route('/', subdomain='home')
def homehome():
    return 'this is subdomain home'

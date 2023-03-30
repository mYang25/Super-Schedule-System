from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    """Return homepage template"""
    """return render_template('index.html')"""
    return("Hello World!")

@app.route('/jiejie')
def jiejie():
    return("Hello Jiejie!")

"""@app.route('/schedule')
def run():"""

app.run(host='0.0.0.0', port=50100, debug=True)
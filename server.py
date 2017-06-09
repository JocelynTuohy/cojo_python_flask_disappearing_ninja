from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def allNinjas():
    return render_template('allNinjas.html')

@app.route('/ninja/<color>')
def thisNinja(color):
    return render_template('thisninja.html', color=color)



app.run(debug=True)
# Nothing after the debug line will be read.

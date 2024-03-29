# -*- coding: cp1252 -*-
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name): 
    return "Hola %s" % name    

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nombre']
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get['nombre']
        return redirect(url_for('success', name = user))

if __name__ == "__main__":
    app.run(debug = True)

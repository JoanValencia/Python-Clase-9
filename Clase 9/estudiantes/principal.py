# -*- coding: cp1252 -*-
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def estudiantes():
    return render_template('estudiantes.html')

@app.route('/resultados', methods=['POST', 'GET'])
def resultados():
    if request.method == 'POST':
        res = request.form
        return render_template('resultados.html', res = res)

if __name__ == "__main__":
    app.run(debug = True)

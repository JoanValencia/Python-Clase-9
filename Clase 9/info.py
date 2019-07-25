# -*- coding: cp1252 -*-
from flask import Flask
app = Flask (__name__)

@app.route("/entero/<int:valor>")
def entero(valor): 
    return "Hello %d" % valor    # %d = dígito

@app.route('/flotante/<float:valor>')
def flotante(valor):
    return "Hello %f" % valor     # %f = flotante

if __name__ == "__main__":
    app.run(debug = True)

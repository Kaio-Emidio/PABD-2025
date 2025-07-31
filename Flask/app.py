from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    nome = "Wolyo"
    sobrenome = "Sei la"
    frutas = ['banana', 'maçã', 'abacate']
    return render_template("inicio.html", n=nome, sn=sobrenome, f=frutas)
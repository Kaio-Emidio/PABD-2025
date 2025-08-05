from flask import Flask, render_template, request
from utils import ConectarBD, InserirAlterarRemover

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('form.html')

@app.route("/envioFormulario", methods=['POST'])
def envio():
    n = request.form.get('nome')
    c = request.form.get('cidade')
    dn = request.form.get('nascimento')

    if n == '':
        n = None
    if c == '':
        c = None
    if dn == '':
        dn = None

    sql = "INSERT INTO pessoa (nome, cidade, nascimento) \
        VALUES (%s, %s, %s)"

    dados = (n, c, dn)

    InserirAlterarRemover(sql, dados)

    return render_template('sucesso.html')

@app.route('/remover')
def remover():
    return render_template('remover.html')

@app.route('/formRemover', methods=['POST'])
def formRemover():
    nr = request.form.get('nomeR')

    if nr == '':
        nr = None

    sql = "DELETE FROM pessoa \
           WHERE nome = %s;"
    
    dados = (nr,)

    InserirAlterarRemover(sql, dados)

    return render_template('sucesso.html')

# @app.route('/alterarcidade')
# def alterar():
#     return render_template('alterarcidade.html')
from flask import Flask, render_template
from mysql.connector import connection

app = Flask(__name__)

# Processo básico de transação:
# 1 - Conexão
# 2 - Cursor
# 3 - SQL + Dados
# 4 - Execute
# 5 - Commit

# Processo básico de Consulta
# 1 - Conexão
# 2 - Cursor
# 3 - SQL + Dados
# 4 - Execute
# 5 - Mostrar


@app.route('/')
def inicio():
    # CONECTANDO AO BANCO
    cnx = connection.MySQLConnection(
        user = 'root',
        password = 'labinfo',
        database = 'brasil',
        host = '127.0.0.1'
    )

    # DEFINIR O CURSOR
    cursor = cnx.cursor(dictionary=True)

    # QUERY SQL
    sql = 'select cidade.nome, estado.uf from cidade, estado where estado.id = cidade.uf and estado.uf="RN"'
    cursor.execute(sql)

    resultado = cursor.fetchall()

    return render_template('table.html', banco = resultado)
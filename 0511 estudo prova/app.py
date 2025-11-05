from flask import Flask, render_template
from mysql.connector import connection

app = Flask(__name__)

def conectar():
    cnx = connection.MySQLConnection(
        user = 'root',
        password = 'labinfo',
        host = '127.0.0.1',
        database = 'academico'
    )

    return cnx

@app.route('/6')
def seis():
    cnx = conectar()
    cursor = cnx.cursor(dictionary=True)

    sql = "SELECT alunos.nome AS aluno, cursos.nome AS curso, matriculas.status \
	       FROM alunos, cursos, matriculas \
	       WHERE alunos.aluno_id=matriculas.aluno_id AND \
		         cursos.curso_id=matriculas.curso_id;"
    
    cursor.execute(sql)
    resultado = cursor.fetchall()

    return render_template('questao.html', bd = resultado)

if __name__ == '__main__':
    app.run(debug=True)
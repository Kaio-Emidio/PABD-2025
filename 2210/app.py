from flask import Flask, render_template
from mysql.connector import connection

app = Flask(__name__)

def conexao():
    cnx = connection.MySQLConnection(
        user = 'root',
        password = 'labinfo',
        host = '127.0.0.1',
        database = 'academico'
    )
    return cnx

@app.route('/')
def inicio():
    return 'Olá'

@app.route('/<q>')
def questao(q):
    cnx = conexao()
    cursor = cnx.cursor(dictionary=True)
    resultado = None
    if q == '1':
        sql = "SELECT alunos.nome, alunos.cidade \
	        FROM alunos \
	        ORDER BY alunos.nome ASC"
    elif q == '2':
        sql = "SELECT alunos.aluno_id, alunos.nome, alunos.email \
	        FROM alunos \
	        WHERE alunos.nome LIKE 'A%'"
    elif q == '3':
        sql = "SELECT alunos.nome, alunos.cidade, alunos.nota_media \
	        FROM alunos \
	        WHERE alunos.nota_media > 8.0"
    elif q == '4':
        sql = "SELECT alunos.nome, alunos.nota_media \
	        FROM alunos \
	        WHERE alunos.nota_media < 7.0"
    elif q == '5':
        sql = "SELECT COUNT(*) AS quantidade \
	        FROM alunos \
	        WHERE alunos.cidade = 'Natal'"
    elif q == '6':
        sql = "SELECT alunos.nome AS aluno, cursos.nome AS curso, matriculas.status \
	        FROM alunos, cursos, matriculas \
	        WHERE alunos.aluno_id=matriculas.aluno_id AND \
		    cursos.curso_id=matriculas.curso_id"
    elif q == '7':
        sql = "SELECT alunos.nome AS aluno, cursos.nome AS curso, matriculas.data_matricula \
	        FROM alunos, cursos, matriculas \
	        WHERE alunos.aluno_id=matriculas.aluno_id AND \
		    cursos.curso_id=matriculas.curso_id AND \
            matriculas.status = 'Ativa' AND \
            cursos.preco > 700"
    elif q == '8':
        sql = "SELECT alunos.nome AS aluno, cursos.nome AS curso, matriculas.status \
	        FROM alunos, cursos, matriculas \
	        WHERE alunos.aluno_id=matriculas.aluno_id AND \
		    cursos.curso_id=matriculas.curso_id AND \
            cursos.area = 'Tecnologia'"

    cursor.execute(sql)

    if q == '5':
        resultado = cursor.fetchone()
    else:
        resultado = cursor.fetchall()
    
    return render_template('questao.html', bd = resultado, questao = q)
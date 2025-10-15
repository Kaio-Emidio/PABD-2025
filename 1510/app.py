from flask import Flask, render_template
from mysql.connector import (connection)

app = Flask(__name__)

cnx = connection.MySQLConnection(
    user='root', 
    password='labinfo', 
    host='127.0.0.1', 
    database='academico'
    )
    
@app.route('/')
def inicio():
    return 'Olá'

@app.route('/um')
def um():
    cursor = cnx.cursor(dictionary=True)

    sql = "select nome, cidade from alunos order by nome ASC;"

    cursor.execute(sql)

    resultado = cursor.fetchall()

    return render_template('um.html', banco = resultado)

@app.route('/dois')
def dois():
    cursor = cnx.cursor(dictionary=True)

    sql = "select aluno_id, nome, email from alunos where nome like 'A%';"

    cursor.execute(sql)

    resultado = cursor.fetchall()

    return render_template('dois.html', banco = resultado)

@app.route('/tres')
def tres():
    cursor = cnx.cursor(dictionary=True)

    sql = "select nome, cidade, nota_media from alunos where nota_media > 8;"

    cursor.execute(sql)

    resultado = cursor.fetchall()

    return render_template('tres.html', banco = resultado)

@app.route('/quatro')
def quatro():
    cursor = cnx.cursor(dictionary=True)

    sql = "select nome, nota_media from alunos where nota_media < 7;"

    cursor.execute(sql)

    resultado = cursor.fetchall()

    return render_template('quatro.html', banco = resultado)

@app.route('/cinco')
def cinco():
    cursor = cnx.cursor(dictionary=True)

    sql = "select count(*) as Numero from alunos where cidade = 'Natal';"

    cursor.execute(sql)

    resultado = cursor.fetchone()

    return render_template('cinco.html', banco = resultado)

@app.route('/seis')
def seis():
    cursor = cnx.cursor(dictionary=True)

    sql = "select alunos.nome as 'Nome do aluno', cursos.nome as 'Nome do curso', matriculas.status from alunos, cursos, matriculas where alunos.aluno_id = matriculas.aluno_id and matriculas.curso_id = cursos.curso_id order by alunos.nome;"

    cursor.execute(sql)

    resultado = cursor.fetchall()

    return render_template('seis.html', banco = resultado)

@app.route('/sete')
def sete():
    cursor = cnx.cursor(dictionary=True)

    sql = "select alunos.nome as 'Nome do aluno', cursos.nome as 'Nome do curso', matriculas.data_matricula from alunos, cursos, matriculas where alunos.aluno_id = matriculas.aluno_id and matriculas.curso_id = cursos.curso_id and matriculas.status = 'Ativa' and cursos.preco > 700;"

    cursor.execute(sql)

    resultado = cursor.fetchall()

    return render_template('sete.html', banco = resultado)

@app.route('/oito')
def oito():
    cursor = cnx.cursor(dictionary=True)

    sql = "select alunos.nome as 'Nome do aluno', cursos.nome as 'Nome do curso', matriculas.status from alunos, cursos, matriculas where alunos.aluno_id = matriculas.aluno_id and matriculas.curso_id = cursos.curso_id and cursos.area = 'Tecnologia';"

    cursor.execute(sql)

    resultado = cursor.fetchall()

    return render_template('oito.html', banco = resultado)


if __name__ == '__main__':
    app.run(debug=True)
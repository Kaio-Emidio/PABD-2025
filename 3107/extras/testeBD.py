from mysql.connector import (connection)

cnx = connection.MySQLConnection(
    user='root', 
    password='labinfo', 
    host='127.0.0.1', 
    database='cliente'
    )

cursor = cnx.cursor()

sql = "INSERT INTO pessoa (nome, cidade, nascimento) \
    VALUES (%s, %s, %s)"

nome = 'Kaio'
cidade = 'Ceará-Mirim'
nasc = '2007-08-02'
dados = (nome, cidade, nasc)

cursor.execute(sql, dados)
cnx.commit()

cnx.close()
from mysql.connector import (connection)
from dotenv import load_dotenv
import os

load_dotenv()

def ConectarBD():
    cnx = connection.MySQLConnection(
    user=os.getenv('USERDB'), 
    password=os.getenv('PASSDB'), 
    host='127.0.0.1', 
    database=os.getenv('NAMEDB')
    )

    return cnx
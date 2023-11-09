import os
import mysql.connector
from flask import Flask

def init_db_connector():
    config = {
        'user' : os.environ.get('MYSQL_USER'),
        'password': os.environ.get('MYSQL_PASSWORD'),
        'database': os.environ.get('MYSQL_DB'),
        'host': os.environ.get('MYSQL_HOST'),
        'raise_on_warnings': True
    }
    cnx = mysql.connector.connect(**config)
    return cnx

db = init_db_connector()

# Test
cursor = db.cursor()
cursor.execute("SELECT * from tasks")
print([x for x in cursor])
cursor.close()

app = Flask(__name__)
from app import routes



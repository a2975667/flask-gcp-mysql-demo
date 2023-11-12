import os
import sys
import mysql.connector
from flask import Flask

def init_db_connector():
    database = os.environ.get('MYSQL_DB')
    config = {
        'user' : os.environ.get('MYSQL_USER'),
        'password': os.environ.get('MYSQL_PASSWORD'),
        # 'database': os.environ.get('MYSQL_DB'),
        'host': os.environ.get('MYSQL_HOST'),
        'raise_on_warnings': True
    }
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(database))
        cursor.execute("USE {}".format(database))
        cursor.execute("""
              CREATE TABLE tasks (
                    id int NOT NULL AUTO_INCREMENT,
                    task varchar(255) NOT NULL,
                    status char(30),
                    PRIMARY KEY (id));
                """)

        cnx.close()
    except Exception as e:
        print(e)
        
    config['database'] = database
    cnx = mysql.connector.connect(**config)
    return cnx

db = init_db_connector()

app = Flask(__name__)
from app import routes



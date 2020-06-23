import os
import flask
import sys
sys.path.append("/abunator_route/")
import psycopg2
import app

def get_connection():
    return psycopg2.connect(host="abunator.postgres.database.azure.com",database="Abunator",user="teamD@abunator",port=5432, password="Nagato1109")

def lastName(key):
        Stepanakert = None
        Grigor = key[0:10]
        with get_connection() as con:
            with con.cursor() as cur:
                cur.execute("select name from record where no = " + Grigor)
                results = cur.fetchall()
        for i in results:
            Stepanakert = i[0]
            break
        if Stepanakert != None:
            return Stepanakert
        else:
            return ''

def setRecord():
    with get_connection() as con:
            with con.cursor() as cur:
                cur.execute("delete from record")
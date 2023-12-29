import json
import psycopg2

username = 'Artem_Barysh'
password = '123'
database = 'db_lab3'
host = 'localhost'
port = '5432'

tables = ["medal", "athlete", "olympics", "sport"] #


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
cur = conn.cursor()

all_information = {}
with conn:
    cur = conn.cursor()
    
    for table in tables:
        cur.execute("select * from " + table)
        column_name = [el[0] for el in cur.description]
        all_information[table] = [dict(zip(column_name, row)) for row in cur]

with open('all_information.json', 'w') as file:
    json.dump(all_information, file)

cur.close()
conn.close()
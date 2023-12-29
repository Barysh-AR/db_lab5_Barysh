
import psycopg2
import csv

username = 'Artem_Barysh'
password = '123'
database = 'db_lab3'
host = 'localhost'
port = '5432'


tables = ["medal", "athlete", "olympics", "sport"]


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
cur = conn.cursor()

for table in tables:
    cur.execute("select * from " + table)

    with open(table + ".csv", 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        first_list = []
        for el in cur.description:
            first_list += [el[0]]
        csv_writer.writerow(first_list)

        for row in cur:
            csv_writer.writerow (row)

cur.close()
conn.close()
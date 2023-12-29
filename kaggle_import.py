import psycopg2
import csv

username = 'Artem_Barysh'
password = '123'
database = 'db_lab3'
host = 'localhost'
port = '5432'

CSV_FILE = "summer.csv"

query_clean = '''
DELETE FROM medal;
DELETE FROM athlete;
DELETE FROM olympics;
DELETE FROM sport;
'''



list_medal = []
list_athlete = []
list_olympics = []
list_sport = []

def add_to_list (list1, qur):
    if qur not in list1: list1 += [qur]

with open(CSV_FILE, 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    
    for i, row in enumerate(reader):
        Year,City,Sport,Discipline,Athlete,Country,Gender,Event,Medal =row
        
        iter_athlete  = [Athlete,Country,Gender]
        iter_olympics = [int(Year),City]
        iter_sport    = [Sport,Discipline,Event]
        ite_medal     = [Medal]

        add_to_list (list_athlete  , iter_athlete)
        add_to_list (list_olympics , iter_olympics)
        add_to_list (list_sport    , iter_sport)

        index_olympics = Year
        index_athlete  = list_athlete.index(iter_athlete) +1
        index_sport    = list_sport.index(iter_sport) +1

        list_medal += [ite_medal + [index_athlete, index_olympics, index_sport]]


        
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()
    cur.execute(query_clean)

    query_imput = '''INSERT INTO Olympics(Olymp_year, city) VALUES (%s, %s)'''
    for el in list_olympics:
        cur.execute(query_imput, (el[0],el[1]))

    query_imput = '''INSERT INTO Athlete(Athlete_name, country, gender, Athlete_id) VALUES (%s, %s, %s, %s)'''
    i = 1
    for el in list_athlete:
        cur.execute(query_imput, (el[0],el[1],el[2],i))
        i +=1

    query_imput = '''INSERT INTO Sport(Sport, discipline, sport_event, sport_id) VALUES (%s, %s, %s, %s)'''
    i = 1
    for el in list_sport:
        cur.execute(query_imput, (el[0],el[1],el[2],i))
        i +=1

    query_imput = '''INSERT INTO Medal (medal_type, medal_id, sport_id, olymp_year, athlete_id) VALUES (%s, %s, %s, %s, %s)'''
    i = 1
    for el in list_medal:
        cur.execute(query_imput, (el[0],i,el[3],el[2],el[1]))
        i +=1


print("Все додано успішно")
cur.close()
conn.close()
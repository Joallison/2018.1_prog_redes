import psycopg2
conn = psycopg2.connect("dbname='db_alunos' user='postgres' host='localhost'")
cur = conn.cursor()
cur.execute("SELECT * FROM alunos")
records = cur.fetchall()
for row in records:
    media = ((row[2] * 2) + (row[3] * 3)) / 5
    print("Matricula:", row[0],"Disciplina:",row[1],"Nota 1:", row[2],"Nota 2:", row[3], "\n A média é:", media)

conn.commit()
cur.close()
conn.close()
exit()

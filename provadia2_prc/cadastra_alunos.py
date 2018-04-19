import psycopg2
import sys
conn = psycopg2.connect("dbname='db_alunos' user='postgres' host='localhost'")
cur = conn.cursor()

argumentos = sys.argv

if len(argumentos) == 1:
    matricula= int(input("Digite sua matricula: "))
    nomedisciplina = input("Digite o nome da disciplina: ")
    nota1 = input("Digite a nota 1:")
    nota2 = input("Digite a nota 2: ")
else:
   len(argumentos)
   matricula = argumentos[1]
   nomedisciplina = argumentos[2]
   nota1 = argumentos[3]
   nota2 = argumentos[4]

cur.execute("INSERT INTO alunos (matricula, nome_disciplina, nota1, nota2) VALUES (%s, '%s', %s, %s);" %(matricula,nomedisciplina,nota1,nota2))
conn.commit()
cur.close()
conn.close()
exit()
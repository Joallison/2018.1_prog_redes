import psycopg2
conexao = "dbname=db_alunos user=postgres host=localhost"

def principal():
	criarBanco()


def criarBanco():
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
    conn = psycopg2.connect("dbname=postgres user=postgres host=localhost")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute('CREATE DATABASE db_alunos')
    conn = psycopg2.connect(conexao)
    cur = conn.cursor()
    cur.execute("CREATE TABLE alunos (matricula integer NOT NULL,nome_disciplina text,nota1 numeric,nota2 numeric);")
    conn.commit()
    conn.close()
	
if __name__ == "__main__": principal()
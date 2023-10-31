import sqlite3
conn = sqlite3.connect("db_maquinario.db")
cursor = conn.cursor()

cursor.execute('CREATE TABLE maquinarios ( ID int primary key NOT NULL , produto varchar(35) DEFAULT NULL, descricao varchar(100) DEFAULT NULL, custo float DEFAULT NULL, disponibilidade tinyint(1) DEFAULT NULL)')
conn.commit()

#cursor.execute('Select * from aluguel, cadastro_cliente')
#print(cursor.fetchall())
import sqlite3
conn = sqlite3.connect("db_maquinario.db")
cursor = conn.cursor()

print("tudo certo")

ID = input("Digite a ID do produto:")
if cursor.execute('SELECT quantidade FROM estoque WHERE id = ?',ID) > 0:
    print("teste")
    
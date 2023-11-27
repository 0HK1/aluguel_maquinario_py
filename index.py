import sqlite3
import os
from datetime import datetime
conn = sqlite3.connect("db_maquinario.db")
cursor = conn.cursor()




#cursor.execute('CREATE TABLE estoque (id_tipo_maqui INTEGER PRIMARY KEY AUTOINCREMENT, nome_produto VARCHAR(50) NOT NULL, quantidade INT NOT NULL, preço_dia REAL NOT NULL);')

#cursor.execute('CREATE TABLE maquinario (id_uni_maquinario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, disponibilidade BOOL NOT NULL, id_tipo_maqui INTEGER NOT NULL, FOREIGN KEY (id_tipo_maqui)REFERENCES estoque (id_tipo_maqui)ON DELETE NO ACTION ON UPDATE NO ACTION);')

#cursor.execute('CREATE TABLE tb_cliente_cadastro (id_cpf VARCHAR(11) PRIMARY KEY NOT NULL, nome_cliente VARCHAR(45) NOT NULL, email VARCHAR(50) NOT NULL)')

#cursor.execute('CREATE TABLE nf_cliente ( id_nf_locacao INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, id_maquinario_alugado INTEGER NOT NULL, data_saida DATETIME NOT NULL, data_retorno DATETIME, custo_total REAL, id_cpf_cliente VARCHAR(11) NOT NULL, FOREIGN KEY (id_maquinario_alugado) REFERENCES maquinario (id_uni_maquinario) ON DELETE NO ACTION ON UPDATE NO ACTION, FOREIGN KEY (id_cpf_cliente) REFERENCES tb_cliente_cadastrado (id_cpf) ON DELETE NO ACTION ON UPDATE NO ACTION)')

#conn.commit()


#cursor.execute('ALTER TABLE maquinario DROP COLUMN descricao;')

#tabela = 'nf_cliente'
#cursor.execute(f"PRAGMA foreign_key_list({tabela});")
#resultados = cursor.fetchall()
#print(resultados)
#cpf = "12345678901"
#cursor.execute('SELECT id_cpf FROM tb_cliente_cadastro WHERE id_cpf = ?',(cpf,))
#a = cursor.fetchall()
#if a:
#    print(a,"tudo certo")
#elif not a():
#    print("Deu Zebra")


#cursor.executemany('INSERT INTO estoque (nome_produto, quantidade, preço_dia) VALUES (?, ?, ?)', [("Parafusadeira", 5, 30.00), ("Furadeira", 7, 20.00), ("Arebitadeira", 3, 35.50), ("Amperímetro", 20, 10.80), ("Balança", 2, 74.99), ("Trator", 5, 350.00), ("Makita", 3, 25.00), ("MotoSerra", 1, 150.00)])
#conn.commit()

#cursor.executemany('INSERT INTO maquinario (id_tipo_maqui, disponibilidade) VALUES (?, ?)', [(1, True), (1, True), (1, True), (1, True), (1, True), (1, True), (2, True), (2, True), (2, True), (2, True), (2, True), (2, True), (3, True), (3, True), (3, True), (3, True), (3, True), (4, True), (4, True), (4, True), (5, True), (6, True), (6, True), (7, True), (7, True), (7, True), (7, True), (7, True), (7, True), (8, True), (8, True), (8, True), (8, True), (8, True), (8, True), (8, True),])
#conn.commit()
#cursor.execute('ALTER TABLE estoque ADD COLUMN quantidade_disponivel INTEGER')
'''cursor.execute("""
    UPDATE estoque
    SET quantidade_disponivel = (
        SELECT COUNT(*)
        FROM maquinario
        WHERE maquinario.id_tipo_maqui = estoque.id_tipo_maqui AND maquinario.disponibilidade = 1
    )
""")'''
tabela = 'tb_cliente_cadastro'

# Instrução SQL para apagar todos os dados da tabela
sql = f'DELETE FROM {tabela}'

# Executar a instrução SQL
cursor.execute(sql)

# Commit para aplicar as mudanças
conn.commit()

# Fechar a conexão
conn.close()
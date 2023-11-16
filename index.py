import sqlite3
import os
conn = sqlite3.connect("db_maquinario_cliente.db")
cursor = conn.cursor()




#cursor.execute('CREATE TABLE estoque ( id_tipo_maqui INT NOT NULL PRIMARY KEY, nome_produto VARCHAR(50) NOT NULL, quantidade INT NOT NULL)')
#cursor.execute('CREATE TABLE maquinario (id_uni_maquinario INTEGER NOT NULL PRIMARY KEY,descricao VARCHAR(50),custo REAL NOT NULL, disponibilidade BOOL NOT NULL,id_tipo_maqui INTEGER NOT NULL, FOREIGN KEY (id_tipo_maqui)REFERENCES estoque (id_tipo_maqui)ON DELETE NO ACTION ON UPDATE NO ACTION);')
#cursor.execute('CREATE TABLE tb_cliente_cadastro (id_cpf VARCHAR(11) PRIMARY KEY NOT NULL, nome_cliente VARCHAR(45) NOT NULL, email VARCHAR(50) NOT NULL, senha VARCHAR(20) NOT NULL)')
#cursor.execute('ALTER TABLE estoque ADD COLUMN preço_dia REAL NOT NULL;')
#cursor.execute('CREATE TABLE nf_cliente ( id_nf_locacao INTEGER NOT NULL PRIMARY KEY, id_maquinario_alugado INTEGER NOT NULL, data_saida DATETIME NOT NULL, data_retorno DATETIME NOT NULL, custo_total REAL NOT NULL, id_cpf_cliente VARCHAR(11) NOT NULL, FOREIGN KEY (id_maquinario_alugado) REFERENCES maquinario (id_uni_maquinario) ON DELETE NO ACTION ON UPDATE NO ACTION, FOREIGN KEY (id_cpf_cliente) REFERENCES tb_cliente_cadastrado (id_cpf) ON DELETE NO ACTION ON UPDATE NO ACTION)')
#cursor.execute('ALTER TABLE new_table RENAME TO nf_cliente;')
#conn.commit()

tabela = 'nf_cliente'
cursor.execute(f"PRAGMA foreign_key_list({tabela});")
resultados = cursor.fetchall()
print(resultados)

#cursor.execute('Select * from aluguel, cadastro_cliente')
#print(cursor.fetchall())
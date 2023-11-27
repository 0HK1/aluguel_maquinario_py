import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from datetime import datetime
conn = sqlite3.connect("db_maquinario.db")
cursor = conn.cursor()

#BANCO DE DADOS, E SUAS IMPLEMENTAÇÕES NO CÓDIGO, DESENVOLVIDO POR JUAN TANAN E DAVI BESERRA
#IMPLEMENTAÇÃO DO FRONT E SUAS LÓGICA FOI DESENVOLIDO POR EDUARDO MIGUEL E NATANAEL HENRIQUE
#SERA ESCRITO UM COMENTÁRIO A RESPEITO DO AUTOR(ES) DE CADA FUNÇÃO

class Aluguel_De_MaquinarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu")
        self.root.geometry("400x400")

        self.btn_cadastro = tk.Button(self.root, text="Cadastro", command=self.abrir_pagina_cadastro, width=20)
        self.btn_cadastro.pack(pady=10)

        self.btn_locacao = tk.Button(self.root, text="Locação", command=self.abrir_pagina_locacao, width=20)
        self.btn_locacao.pack(pady=10)

        self.btn_validacao = tk.Button(self.root, text="Pagamento NFe", command=self.abrir_pagina_validacao, width=20)
        self.btn_validacao.pack(pady=10)

        self.btn_lista_maquinarios = tk.Button(self.root, text="Lista de Maquinários", command=self.abrir_pagina_lista_maquinarios, width=20)
        self.btn_lista_maquinarios.pack(pady=10)
#MIGUEL
    def abrir_pagina_cadastro(self):
        self.cadastro_window = tk.Toplevel(self.root)
        self.cadastro_window.title("Cadastro")
        self.cadastro_window.geometry("300x300")
        
        self.label_nome = tk.Label(self.cadastro_window, text="Nome:")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(self.cadastro_window)
        self.entry_nome.pack()

        self.label_email = tk.Label(self.cadastro_window, text="Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(self.cadastro_window)
        self.entry_email.pack()

        self.label_cpf = tk.Label(self.cadastro_window, text="CPF:")
        self.label_cpf.pack()
        self.entry_cpf = tk.Entry(self.cadastro_window)
        self.entry_cpf.pack()

        self.btn_cadastrar_usuario = tk.Button(self.cadastro_window, text="Cadastrar Usuário", command=self.cadastrar_usuario)
        self.btn_cadastrar_usuario.pack()
#MIGUEL
    def cadastrar_usuario(self):
        nome = str(self.entry_nome.get())
        email = str(self.entry_email.get())
        cpf = str(self.entry_cpf.get())

        cursor.execute('INSERT INTO tb_cliente_cadastro (id_cpf, nome_cliente, email) VALUES (?, ?, ?)', (cpf, nome, email))
        conn.commit()
        cursor.execute('SELECT nome_cliente FROM tb_cliente_cadastro WHERE id_cpf = ?',(cpf,))
        nome_cadastrado_tupla = cursor.fetchall()
        nome_cadastrado = nome_cadastrado_tupla[0][0]
        mensagem = f"Usuário {nome_cadastrado} cadastrado com sucesso!"
        

        messagebox.showinfo("Cadastro", mensagem)
#MIGUEL FRON // DAVI IMPLEMENTAÇÃO BANCO
    def abrir_pagina_locacao(self):
        self.locacao_window = tk.Toplevel(self.root)
        self.locacao_window.title("Locação")
        self.locacao_window.geometry("300x150")

        self.label_cpf_locacao = tk.Label(self.locacao_window, text="CPF:")
        self.label_cpf_locacao.pack()
        self.entry_cpf_locacao = tk.Entry(self.locacao_window)
        self.entry_cpf_locacao.pack()

        self.label_id_maquina = tk.Label(self.locacao_window, text="ID da Máquina:")
        self.label_id_maquina.pack()
        self.entry_id_maquina = tk.Entry(self.locacao_window)
        self.entry_id_maquina.pack()

        self.btn_alugar = tk.Button(self.locacao_window, text="Alugar", command=self.efetuar_aluguel)
        self.btn_alugar.pack()
#MIGUEL
    def efetuar_aluguel(self):
        cpf = self.entry_cpf_locacao.get()
        id_maquina = self.entry_id_maquina.get()
        
        cursor.execute('SELECT id_cpf FROM tb_cliente_cadastro WHERE id_cpf = ?',(cpf,))
        valida_cpf = cursor.fetchone()

        cursor.execute('SELECT id_uni_maquinario FROM maquinario WHERE id_uni_maquinario = ? and disponibilidade = 1',(id_maquina,))
        valida_maq = cursor.fetchone()

        if valida_cpf and str(valida_cpf[0]) == cpf and valida_maq and str(valida_maq[0]) == id_maquina:
            messagebox.showinfo("Aluguel", f"Máquina {id_maquina} alugada com sucesso!")
            data_saida = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            cursor.execute("INSERT INTO nf_cliente (id_maquinario_alugado, data_saida, id_cpf_cliente) VALUES (?, ?, ?)",(id_maquina, data_saida, cpf))
            cursor.execute('UPDATE maquinario SET disponibilidade = 0 WHERE id_uni_maquinario = ?',(id_maquina,))
            conn.commit()

        elif not valida_maq:
            messagebox.showerror("Aluguel", "ERRO BUSCA MAQUINA!")

        elif not valida_cpf:
            messagebox.showerror("Aluguel", "ERRO NA BUSCA DO CPF") 

        else:
            messagebox.showerror("Aluguel", "ERRO NÃO IDENTIFICADO")
            print(valida_cpf)
            print(valida_maq)

        # Aqui é onde a interação com o banco de dados para registrar o aluguel deve ser feita
        # Você vai usar as variáveis 'cpf' e 'id_maquina' para registrar o aluguel no banco de dados
    
        # Você tambem pode usar ambas as variáveis 'cpf' de cadastro e alugar maquinario para armazenalas e juntalas (eu acho que deve ir sozinho)  
#MIGUEL FRONT // DAVI IMPLEMENTAÇÃO BANCO
    def abrir_pagina_validacao(self):
        self.validacao_window = tk.Toplevel(self.root)
        self.validacao_window.title("Pagamento NFe")
        self.validacao_window.geometry("300x150")

        self.label_id_nf_locacao = tk.Label(self.validacao_window, text="Digite sua NFe:")
        self.label_id_nf_locacao.pack()
        self.entry_id_nf_locacao = tk.Entry(self.validacao_window)
        self.entry_id_nf_locacao.pack()

        self.btn_validar_disponibilidade = tk.Button(self.validacao_window, text="Visualizar NFe", command=self.validar_disponibilidade)
        self.btn_validar_disponibilidade.pack()
#HENRIQUE FRONT
    def validar_disponibilidade(self):

        data_retorno = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        #DIA RETORNO A LOJA//INCLUIR NA NF

        id_nf_locacao = self.entry_id_nf_locacao.get()
        #IDENTIFICAR A NF

        cursor.execute('''
            SELECT data_saida FROM nf_cliente WHERE id_nf_locacao = ?
                       ''',(id_nf_locacao,))
        data_saida_tupla = cursor.fetchone()
        data_saida_str = data_saida_tupla[0]
        #PUXA A DATA QUE SAIU DA LOJA

        data_saida = datetime.strptime(data_saida_str, '%Y-%m-%d %H:%M:%S.%f')
        
        cursor.execute('''                       
            SELECT estoque.preço_dia
            FROM nf_cliente
            JOIN maquinario ON nf_cliente.id_maquinario_alugado = maquinario.id_uni_maquinario
            JOIN estoque ON maquinario.id_tipo_maqui = estoque.id_tipo_maqui WHERE id_nf_locacao = ?
            ''',(id_nf_locacao,))
        valor_dia = cursor.fetchone()
        #PUXA O VALOR POR DIA
        dias_corridos = -1 * (datetime.strptime(data_retorno, '%Y-%m-%d %H:%M:%S.%f') - data_saida).days
        
        if not dias_corridos:
            dias_corridos = 1

        custo_total = valor_dia[0] * dias_corridos
        #CALCULA O CUSTO TOTAL
        cursor.execute('''
            SELECT id_maquinario_alugado
            FROM nf_cliente
            WHERE id_nf_locacao = ?
                       ''',(id_nf_locacao))
        id_maqui_tupla = cursor.fetchone()
        id_maqui = id_maqui_tupla[0]

        cursor.execute('''
            UPDATE maquinario
            SET disponibilidade = 1
            WHERE id_uni_maquinario = ?
                       ''',(id_maqui,))

        cursor.execute('''
            UPDATE nf_cliente 
            SET data_retorno = ?,
            custo_total = ?
            WHERE id_nf_locacao = ?
                       ''',(data_retorno, custo_total, id_nf_locacao))
        conn.commit()
        #print(custo_total, data_saida, valor_dia, dias_corridos)

        cursor.execute('''
            SELECT disponibilidade
            FROM maquinario
            WHERE id_uni_maquinario = ?
                       ''', id_maqui)
        disponibilidade_tupla = cursor.fetchone()
        disponibilidade = disponibilidade_tupla[0]
       
        if disponibilidade:
            messagebox.showinfo("NFe Cliente", f"Nota fiscal no valor de {custo_total} para pagar no caixa!")
        else:
            messagebox.showwarning("Validação de Disponibilidade", f"A máquina {id_nf_locacao} não está disponível.")

        # ...

        # Adicione esta parte no método _init_ para vincular o botão de validação de disponibilidade à função correspondente
        self.btn_validacao = tk.Button(self.root, text="Validação de Disponibilidade", command=self.abrir_pagina_validacao, width=20)
        self.btn_validacao.pack(pady=10)
#HENRIQUE FRONT // DAVI IMPLEMENTAÇÃO BANCO
    def abrir_pagina_lista_maquinarios(self):
        self.lista_maquinarios_window = tk.Toplevel(self.root)
        self.lista_maquinarios_window.title("Lista de Maquinários Disponíveis")
        self.lista_maquinarios_window.geometry("500x300")

    # Consulta para recuperar os maquinários disponíveis e suas quantidades
        cursor.execute("SELECT id_tipo_maqui, nome_produto, quantidade FROM estoque WHERE id_tipo_maqui > 0")
        maquinarios_disponiveis = cursor.fetchall()

        table = ttk.Treeview(self.lista_maquinarios_window)
        table['columns'] = ('ID do Maquinário', 'Nome do Maquinário', 'Quantidade Disponível')

        table.column('#0', width=0, stretch=tk.NO)
        table.column('ID do Maquinário', anchor=tk.W, width=150)
        table.column('Nome do Maquinário', anchor=tk.W, width=200)
        table.column('Quantidade Disponível', anchor=tk.W, width=150)

        table.heading('#0', text='', anchor=tk.W)
        table.heading('ID do Maquinário', text='ID do Maquinário', anchor=tk.W)
        table.heading('Nome do Maquinário', text='Nome do Maquinário', anchor=tk.W)
        table.heading('Quantidade Disponível', text='Quantidade Disponível', anchor=tk.W)

        for maquinario in maquinarios_disponiveis:
            table.insert('', tk.END, values=maquinario)

        table.pack(expand=tk.YES, fill=tk.BOTH)
#MIGUEL
if __name__ == "__main__":
    root = tk.Tk()
    app = Aluguel_De_MaquinarioApp(root)
    root.mainloop()

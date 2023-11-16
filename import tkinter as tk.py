import sqlite3
import tkinter as tk
from tkinter import messagebox

class AluguelMaquinarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aluguel de Maquinário")
        
        conn = sqlite3.connect("db_maquinario.db")
        cursor = conn.cursor()
        
        # Dicionário para rastrear maquinários disponíveis e indisponíveis
        self.maquinarios = {
            "Máquina A": "Disponível",
            "Máquina B": "Indisponível",
            "Máquina C": "Disponível",
            "Máquina D": "Disponível",
            "Máquina E": "Indisponível",  
            "Máquina F": "Disponível",  
        }
        
        # Aqui é a lista de maquinários, ainda falta adicionar mais alguns e uma tabela de quantos estão armazenados
        self.disponiveis = [maquina for maquina, status in self.maquinarios.items() if status == "Disponível"]

        # Rótulos
        self.label_disponiveis = tk.Label(root, text="Maquinários indisponíveis:")
        self.label_disponiveis.pack()
        self.label_indisponiveis = tk.Label(root, text="Maquinários Disponíveis:")
        self.label_indisponiveis.pack()

        # Listbox de maquinários disponíveis
        self.maquinarios_disponiveis_listbox = tk.Listbox(root)
        for maquina in self.disponiveis:
            self.maquinarios_disponiveis_listbox.insert(tk.END, maquina)
        self.maquinarios_disponiveis_listbox.pack()

        # Botão para alugar
        self.alugar_button = tk.Button(root, text="Alugar", command=self.alugar_maquinario)
        self.alugar_button.pack()
    
    def buscar_dados():
        with sqlite3.connect('db_maquinario.db') as conn:
         cursor = conn.cursor()
         cursor.execute("SELECT * FROM usuarios")
         rows = cursor.fetchall()
        return rows

    def alugar_maquinario(self):
        # Verifica se um maquinário foi selecionado
        selected_index = self.maquinarios_disponiveis_listbox.curselection()
        if selected_index:
            maquina_selecionada = self.maquinarios_disponiveis_listbox.get(selected_index)
            if self.maquinarios[maquina_selecionada] == "Disponível":
                messagebox.showinfo("Sucesso", f"Você alugou a {maquina_selecionada}!")
                # Atualiza o status do maquinário selecionado para indisponível
                self.maquinarios[maquina_selecionada] = "Indisponível"
                # Atualiza a lista de maquinários disponíveis
                self.disponiveis = [maquina for maquina, status in self.maquinarios.items() if status == "Disponível"]
                self.maquinarios_disponiveis_listbox.delete(0, tk.END)
                for maquina in self.disponiveis:
                    self.maquinarios_disponiveis_listbox.insert(tk.END, maquina)
            else:
                messagebox.showinfo("Aviso", f"{maquina_selecionada} já está alugada.")
        else:
            messagebox.showinfo("Aviso", "Selecione um maquinário para alugar.")

if __name__ == "__main__":
    db_file = 'db_maquinario.db'
    root = tk.Tk()
    app = AluguelMaquinarioApp(root)
    root.mainloop()
import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


janela = tk.Tk()
janela.title("Cadastro de Clientes")
conexao = sqlite3.connect("clientes.db")
conexao.execute("""CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL
)""")


def limpar_formulario():
    for campo in campos:
        campo.delete(0, tk.END)
    campos[0].focus_set()


def salvar_cliente():
    dados = tuple(campo.get().strip() for campo in campos)
    if not all(dados):
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return
    try:
        with conexao:
            conexao.execute(
                "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)", dados
            )
    except sqlite3.Error as erro:
        messagebox.showerror("Erro ao salvar", str(erro))
        return
    messagebox.showinfo("Sucesso", "Cliente salvo com sucesso!")
    limpar_formulario()


painel = ttk.Frame(janela, padding=12)
painel.pack(fill="both", expand=True)
campos = []
for linha, rotulo in enumerate(("Nome", "Email", "Telefone")):
    ttk.Label(painel, text=rotulo).grid(row=linha, column=0, sticky="w", pady=4)
    campo = ttk.Entry(painel, width=36)
    campo.grid(row=linha, column=1, sticky="ew", padx=6)
    campos.append(campo)
painel.columnconfigure(1, weight=1)
botoes = ttk.Frame(painel)
botoes.grid(row=3, column=0, columnspan=2, pady=8)
ttk.Button(botoes, text="Salvar", command=salvar_cliente).pack(side="left")
ttk.Button(botoes, text="Limpar", command=limpar_formulario).pack(side="left")
campos[0].focus_set()
try:
    janela.mainloop()
finally:
    conexao.close()

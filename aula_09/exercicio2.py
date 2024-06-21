import tkinter as interface
from tkinter import messagebox

janela = interface.Tk()
janela.title("Formulário")
janela.geometry("500x300")


frameForm = interface.Frame(janela)
frameForm.pack()

frameBotao = interface.Frame(janela)
frameBotao.pack()

btnCadastro = interface.Button(frameBotao, text=" Cadastrar ", font=15, bg="#fff")
btnCadastro.grid(row=1, column=1, pady=20)

# FORMULÁRIO
 # Nome
lblNome = interface.Label(frameForm, text="Nome: ", font=15)
lblNome.grid(row=1, column=1, padx=30, pady=10, sticky='w')

txtNome = interface.Entry(frameForm, font=15)
txtNome.grid(row=1, column=2, padx=30, pady=10)

 # Email
lblEmail = interface.Label(frameForm, text="Email: ", font=15)
lblEmail.grid(row=2, column=1, padx=30, pady=10, sticky='w')

txtEmail = interface.Entry(frameForm, font=15)
txtEmail.grid(row=2, column=2, padx=30, pady=10)

 # Idade
lblIdade = interface.Label(frameForm, text="Idade: ", font=15)
lblIdade.grid(row=3, column=1, padx=30, pady=10, sticky='w')

txtIdade = interface.Entry(frameForm, font=15)
txtIdade.grid(row=3, column=2, padx=30, pady=10)

 # Telefone
lblTel = interface.Label(frameForm, text="Telefone: ", font=15)
lblTel.grid(row=4, column=1, padx=30, pady=10, sticky='w')

txtTel = interface.Entry(frameForm, font=15)
txtTel.grid(row=4, column=2, padx=30, pady=10)


janela.mainloop()
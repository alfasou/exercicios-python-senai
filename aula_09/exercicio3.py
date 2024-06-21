import tkinter as interface
from tkinter import messagebox

janela = interface.Tk()
janela.title("Layout Simples")
janela.geometry("500x300")


frameMensagem = interface.Frame(janela)
frameMensagem.pack()

frameForm = interface.Frame(janela)
frameForm.pack()

# MENSAGEM
lblOla = interface.Label(frameMensagem, text="Bem-vindo ao Layout Simples!", font=30)
lblOla.grid(row=1, column=1, pady=10)

btnClica = interface.Button(frameMensagem, text=" Clique Aqui ", font=15, bg="#fff")
btnClica.grid(row=2, column=1, pady=20)

# FORM
txtInput = interface.Entry(frameForm, font=15)
txtInput.grid(row=1, column=1, padx=10, pady=20)

btnLimpa = interface.Button(frameForm, text=" Limpar ", font=15, bg="#fff")
btnLimpa.grid(row=1, column=2, padx=10, pady=20)

janela.mainloop()
import tkinter as interface
from tkinter import messagebox

janela = interface.Tk()
janela.title("Exemplo Frames e Grid")
janela.geometry("400x200")

frameMenu = interface.Frame(janela, bg="blue")#background
frameMenu.pack()

frameInformacoes = interface.Frame(janela)
frameInformacoes.pack()

lblInfo1 = interface.Label(frameInformacoes, text="Info1", font=19)
lblInfo1.grid(row=1, column=1)

lblInfo2 = interface.Label(frameInformacoes, text="Info2", font=19)
lblInfo2.grid(row=1, column=2)

lblInfo3 = interface.Label(frameInformacoes, text="Info3", font=19)
lblInfo3.grid(row=1, column=3)

lblInfo4 = interface.Label(frameInformacoes, text="Info4", font=19)
lblInfo4.grid(row=2, column=1)

lblInfo5 = interface.Label(frameInformacoes, text="Info5", font=19)
lblInfo5.grid(row=2, column=2)

lblInfo6 = interface.Label(frameInformacoes, text="Info6", font=19)
lblInfo6.grid(row=2, column=3)

btn1 = interface.Button(frameMenu, text="Botão 1", font=15)
btn1.grid(row=1, column=1,padx=10)

btn2 = interface.Button(frameMenu, text="Botão 2", font=15)
btn2.grid(row=1, column=2, padx=10)

btn3 = interface.Button(frameMenu, text="Botão 3", font=15)
btn3.grid(row=1, column=3, padx=10)

btn4 = interface.Button(frameMenu, text="Botão 4", font=15)
btn4.grid(row=1, column=4, padx=10)

janela.mainloop()
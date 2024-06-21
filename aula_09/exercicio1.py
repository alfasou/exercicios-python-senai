import tkinter as interface
from tkinter import messagebox

janela = interface.Tk()
janela.title("Calculadora")
janela.geometry("500x300")

listaBotoes = ['7', '8', '9', '÷', '4', '5', '6', '×', '1', '2', '3', '-', '0', '.', '=', '+' ]

qtdLinhas = 4
qtdColunas = 4


frameVisor = interface.Frame(janela)
frameVisor.pack()

frameBotoes = interface.Frame(janela)
frameBotoes.pack()


txtVisor = interface.Entry(frameVisor, font=15)
txtVisor.grid(row=0, column=0, pady=20)

indexTexto = 0

for linha in range(qtdLinhas):
    for coluna in range(qtdColunas):
        textoBotao = listaBotoes[indexTexto]
        btn = interface.Button(frameBotoes, text=textoBotao, font=15, bg="#fff", width=7)
        btn.grid(row=linha, column=coluna, padx=10, pady=10)
        indexTexto += 1

# # BOTÕES
#  # Linha 1
# btn7 = interface.Button(frameBotoes, text="7", font=15, bg="#fff", width=7)
# btn7.grid(row=1, column=1, padx=10, pady=10)

# btn8 = interface.Button(frameBotoes, text="8", font=15, bg="#fff", width=7)
# btn8.grid(row=1, column=2, padx=10, pady=10)

# btn9 = interface.Button(frameBotoes, text="9", font=15, bg="#fff", width=7)
# btn9.grid(row=1, column=3, padx=10, pady=10)

# btnDiv = interface.Button(frameBotoes, text="÷", font=15, bg="#fff", width=7)
# btnDiv.grid(row=1, column=4, padx=10, pady=10)

#  # Linha 2
# btn4 = interface.Button(frameBotoes, text="4", font=15, bg="#fff", width=7)
# btn4.grid(row=2, column=1, padx=10, pady=10)

# btn5 = interface.Button(frameBotoes, text="5", font=15, bg="#fff", width=7)
# btn5.grid(row=2, column=2, padx=10, pady=10)

# btn6 = interface.Button(frameBotoes, text="6", font=15, bg="#fff", width=7)
# btn6.grid(row=2, column=3, padx=10, pady=10)

# btnMult = interface.Button(frameBotoes, text="x", font=15, bg="#fff", width=7)
# btnMult.grid(row=2, column=4, padx=10, pady=10)

#  # Linha 3
# btn1 = interface.Button(frameBotoes, text="1", font=15, bg="#fff", width=7)
# btn1.grid(row=3, column=1, padx=10, pady=10)

# btn2 = interface.Button(frameBotoes, text="2", font=15, bg="#fff", width=7)
# btn2.grid(row=3, column=2, padx=10, pady=10)

# btn3 = interface.Button(frameBotoes, text="3", font=15, bg="#fff", width=7)
# btn3.grid(row=3, column=3, padx=10, pady=10)

# btnSub = interface.Button(frameBotoes, text="-", font=15, bg="#fff", width=7)
# btnSub.grid(row=3, column=4, padx=10, pady=10)

#  # Linha 4
# btn0 = interface.Button(frameBotoes, text="0", font=15, bg="#fff", width=7)
# btn0.grid(row=4, column=1, padx=10, pady=10)

# btnPonto = interface.Button(frameBotoes, text=".", font=15, bg="#fff", width=7)
# btnPonto.grid(row=4, column=2, padx=10, pady=10)

# btnIgual = interface.Button(frameBotoes, text="=", font=15, bg="#fff", width=7)
# btnIgual.grid(row=4, column=3, padx=10, pady=10)

# btnSoma = interface.Button(frameBotoes, text="+", font=15, bg="#fff", width=7)
# btnSoma.grid(row=4, column=4, padx=10, pady=10)



janela.mainloop()
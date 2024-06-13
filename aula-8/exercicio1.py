import tkinter as interface
from tkinter import messagebox

def centralizar_janela(janela):
    largura_janela = 1200
    altura_janela = 600

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2

    janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

def apresentarSoma():
    numero1 = int(txtNum1.get())
    numero2 = int(txtNum2.get())
    messagebox.showinfo("Resultado da Soma", f"{numero1} + {numero2} = {numero1 + numero2}")

def apresentarSubtracao():
    numero1 = int(txtNum1.get())
    numero2 = int(txtNum2.get())
    messagebox.showinfo("Resultado da Subtração", f"{numero1} - {numero2} = {numero1 - numero2}")

def apresentarDivisao():
    numero1 = int(txtNum1.get())
    numero2 = int(txtNum2.get())
    messagebox.showinfo("Resultado da Divisão", f"{numero1} ÷ {numero2} = {numero1 / numero2}")

def apresentarMultiplicacao():
    numero1 = int(txtNum1.get())
    numero2 = int(txtNum2.get())
    messagebox.showinfo("Resultado da Multiplicação", f"{numero1} × {numero2} = {numero1 * numero2}")

def fecharJanela():
    simOuNao = messagebox.askquestion("Fechar Calculadora", "Deseja realmente fechar a calculadora?")

    if simOuNao == "yes":
        janela.destroy()
    
janela = interface.Tk()
janela.title("Calculadora Simples")
centralizar_janela(janela)

lblNum1 = interface.Label(janela, text="Digite um número")
lblNum1.pack()

txtNum1 = interface.Entry(janela)
txtNum1.pack()

lblNum2 = interface.Label(janela, text="Digite outro número")
lblNum2.pack()

txtNum2 = interface.Entry(janela)
txtNum2.pack()

btnSoma = interface.Button(janela, text="+", command=apresentarSoma)
btnSoma.pack(pady=4)

btnSubtracao = interface.Button(janela, text="-", command=apresentarSubtracao)
btnSubtracao.pack(pady=4)

btnDivisao = interface.Button(janela, text="÷", command=apresentarDivisao)
btnDivisao.pack(pady=4)

btnMultiplicacao = interface.Button(janela, text="x", command=apresentarMultiplicacao)
btnMultiplicacao.pack(pady=4)

btnFecharJanela = interface.Button(janela, text="Finalizar", command=fecharJanela)
btnFecharJanela.pack(pady=4)

janela.mainloop()


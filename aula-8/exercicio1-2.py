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

def operacao(operador):
    numero1 = int(txtNum1.get())
    numero2 = int(txtNum2.get())
    mensagem = ''

    if numero2 == 0:
        mensagem = "Não é possível dividir por 0"
    elif operador == "+":
        mensagem = f"{numero1} + {numero2} = {numero1 + numero2}"
    elif operador == "-":
        mensagem = f"{numero1} - {numero2} = {numero1 - numero2}"
    elif operador == "÷":
        mensagem = f"{numero1} ÷ {numero2} = {numero1 / numero2}"
    elif operador == "x": 
        mensagem = f"{numero1} x {numero2} = {numero1 * numero2}"
    else:
        mensagem = "Operador não Reconhecido"
        


    lblResultado.config(text=f'{mensagem}')
    # messagebox.showinfo("Resultado da Operação", f"{mensagem}")


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

btnSoma = interface.Button(janela, text="+", command=lambda: operacao("+"))
btnSoma.pack(pady=4)

btnSubtracao = interface.Button(janela, text="-", command=lambda: operacao("-"))
btnSubtracao.pack(pady=4)

btnDivisao = interface.Button(janela, text="÷", command=lambda: operacao("÷"))
btnDivisao.pack(pady=4)

btnMultiplicacao = interface.Button(janela, text="x", command=lambda: operacao("x"))
btnMultiplicacao.pack(pady=4)

btnFecharJanela = interface.Button(janela, text="Finalizar", command=fecharJanela)
btnFecharJanela.pack(pady=4)

lblResultado = interface.Label(janela, text="Resultado da Operação", font=15)
lblResultado.pack(pady=5)

janela.mainloop()


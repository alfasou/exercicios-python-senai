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

def calculaImc():
    peso = float(txtPeso.get())
    altura = float(txtAltura.get())
    imc = peso / (altura**2)

    if imc < 18.5:
        mensagem = "Você está abaixo do Peso"
    elif 18.5 <= imc <= 24.9:
        mensagem = "Seu peso está Normal"
    elif 25 <= imc < 29.9:
        mensagem = "Você está com Sobrepeso"
    else:
        mensagem = "Você está Obeso"

    messagebox.showinfo("Seu IMC:", f"{mensagem}")

def fecharJanela():
    simOuNao = messagebox.askquestion("Finalizar programa", "Deseja realmente finalizar o programa?")

    if simOuNao == "yes":
        janela.destroy()
    
janela = interface.Tk()
janela.title("Cálculo de IMC (Índice de Massa Corporal)")
centralizar_janela(janela)

lblPeso = interface.Label(janela, text="Digite seu Peso")
lblPeso.pack()

txtPeso = interface.Entry(janela)
txtPeso.pack()

lblAltura = interface.Label(janela, text="Digite a sua Altura")
lblAltura.pack()

txtAltura = interface.Entry(janela)
txtAltura.pack()

btnVerificar = interface.Button(janela, text="Verificar", command=calculaImc)
btnVerificar.pack(pady=4)

btnFecharJanela = interface.Button(janela, text="Finalizar", command=fecharJanela)
btnFecharJanela.pack()

janela.mainloop()
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

def verificaIdade():
    nome = txtNome.get()
    idade = int(txtIdade.get())
    mensagem = ''
    
    if idade >= 18:
        mensagem = f"Olá {nome}!\nVocê é maior de idade!"
    else:
        mensagem = f"Olá {nome}!\nVocê é menor de idade."
    
    messagebox.showinfo("Verificação:", f"{mensagem}")

def fecharJanela():
    simOuNao = messagebox.askquestion("Finalizar programa", "Deseja realmente finalizar o programa?")

    if simOuNao == "yes":
        janela.destroy()
    
janela = interface.Tk()
janela.title("Verificador de Maioridade")
centralizar_janela(janela)

lblNome = interface.Label(janela, text="Digite seu nome")
lblNome.pack()

txtNome = interface.Entry(janela)
txtNome.pack()

lblIdade = interface.Label(janela, text="Digite a sua idade")
lblIdade.pack()

txtIdade = interface.Entry(janela)
txtIdade.pack()

btnVerificarIdade = interface.Button(janela, text="Verificar", command=verificaIdade)
btnVerificarIdade.pack()

btnFecharJanela = interface.Button(janela, text="Finalizar", command=fecharJanela)
btnFecharJanela.pack()

janela.mainloop()
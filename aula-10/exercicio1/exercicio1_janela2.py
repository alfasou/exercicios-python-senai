import tkinter as interface
import exercicio1_janela3
import exercicio1_janela4

janela = None

def abrirCadastro():
    exercicio1_janela3.iniciarJanela()

def abrirSistema():
    exercicio1_janela4.iniciarJanela()

def fecharJanela():
    janela.destroy()

def iniciarJanela():
    global janela
    janela = interface.Tk()
    janela.geometry("350x400")
    janela.title("Menu")

    btnCadastro = interface.Button(janela, text="Cadastro", command=abrirCadastro, font=15, width=30, height=5)
    btnCadastro.pack(pady=10)

    btnSistema = interface.Button(janela, text="Sistema", command=abrirSistema, font=15, width=30, height=5)
    btnSistema.pack(pady=10)

    btnSair = interface.Button(janela, text="Sair", command=fecharJanela, font=15, width=30, height=5)
    btnSair.pack(pady=10)

    janela.mainloop()



if __name__ == "__main__":
    iniciarJanela()
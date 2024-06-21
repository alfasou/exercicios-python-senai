import tkinter as interface
import janela1

def abrirNovaJanela():
    janela.destroy()
    janela1.iniciarJanela()

def iniciarJanela():
    global janela
    janela = interface.Tk()
    janela.geometry("300x300")
    janela.title("Janela 3")

    txtNome = interface.Entry(janela)
    txtNome.pack()

    botao = interface.Button(janela, text="Voltar", command=abrirNovaJanela)
    botao.pack()

    janela.mainloop()

if __name__ == "__main__":
    iniciarJanela()
import tkinter as interface

def iniciarJanela():
    janela = interface.Tk()
    janela.geometry("300x300")
    janela.title("Janela 2")

    botaoAbrirJanela2 = interface.Button(janela, text="Abrir janela 3")
    botaoAbrirJanela2.pack()

    janela.mainloop()



if __name__ == "__main__":
    iniciarJanela()
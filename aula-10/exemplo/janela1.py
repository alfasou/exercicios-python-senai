import tkinter as interface
import janela3

janela = None

def abrirNovaJanela():
    janela.destroy()
    janela3.iniciarJanela()
    

def iniciarJanela():
    global janela
    janela = interface.Tk()
    janela.geometry("300x300")
    janela.title("Titulo")

    botaoAbrirJanela2 = interface.Button(janela, text="Abrir janela 3", command=abrirNovaJanela)
    botaoAbrirJanela2.pack()

    janela.mainloop()



if __name__ == "__main__":
    iniciarJanela()
import tkinter as interface
from tkinter import messagebox
import random

class CampoMinado:
    def __init__(self):
        self.pontos = 0
        self.botoes = []
        self.bombas = []
        self.iniciar_janela()

    def achou_bomba(self, i):
        if i in self.bombas:
            self.botoes[i]['bg'] = '#ff0000'
            self.botoes[i]['state'] = 'disabled'
            self.botoes[i]['text'] = '💣'
            resposta = messagebox.askquestion(title='Bomba encontrada!!! 💥', message='Deseja reiniciar o jogo?')
            if resposta == 'yes':
                self.janela.destroy()
                self.__init__()
            else:
                self.janela.destroy()
        else:
            self.pontos += 1
            self.botoes[i]['bg'] = '#fff'
            self.botoes[i]['state'] = 'disabled'
            self.botoes[i]['text'] = '1'
            self.lbl_pontos.config(text=f'Pontuação {self.pontos}')

    def iniciar_janela(self):
        self.janela = interface.Tk()
        self.janela.geometry('540x450')
        self.janela.title('Campo Minado')

        frame_campo = interface.Frame(self.janela)
        frame_campo.pack()

        frame_pontos = interface.Frame(self.janela)
        frame_pontos.pack()

        qtd_linhas = 5
        qtd_colunas = 5
        qtd_bombas = 5
        qtd_botoes = qtd_linhas * qtd_colunas

        self.bombas = random.sample(range(qtd_botoes), qtd_bombas)

        for linha in range(qtd_linhas):
            for coluna in range(qtd_colunas):
                indice = linha * qtd_colunas + coluna
                btn = interface.Button(frame_campo, font=20, bg='#ccc', width=7, height=3, command=lambda idx=indice: self.achou_bomba(idx))
                btn.grid(row=linha, column=coluna, padx=3, pady=3)
                self.botoes.append(btn)

        self.lbl_pontos = interface.Label(frame_pontos, text=f'Pontuação {self.pontos}', font=15)
        self.lbl_pontos.pack(pady=10)

        self.janela.mainloop()

if __name__ == '__main__':
    CampoMinado()
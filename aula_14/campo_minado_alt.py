import tkinter as interface
from tkinter import messagebox
from tkinter import PhotoImage
import os
import random

janela = None
quantidadeBombas = 5
quantidadeLinhasColunas = 5
pontuacaoGame = 0
lista_botoes = []
posicoes_bombas = random.sample(range(quantidadeLinhasColunas ** 2), quantidadeBombas)
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

def cliqueBotao(posicaoBotao):
    global pontuacaoGame
    botaoSelecionado = lista_botoes[posicaoBotao]
    if posicaoBotao in posicoes_bombas:
        botaoSelecionado.config(image=bombaImagem, state = interface.DISABLED)
        simOuNao = messagebox.askyesno('BOMBAA!','Bomba encontrada\nDeseja reiniciar o jogo?')

        if simOuNao == True:
            reiniciarGame()
        else:
            janela.destroy()
    else:
        botaoSelecionado.config(image=bandeiraImagem, state = interface.DISABLED)
        pontuacaoGame = pontuacaoGame + 1
        lblPontuacao.config(text=f'Pontuação: {pontuacaoGame}')

def reiniciarGame():
    global posicoes_bombas, pontuacaoGame
    pontuacaoGame = 0
    lblPontuacao.config(text=f'Pontuação: 0')
    posicoes_bombas = random.sample(range(quantidadeLinhasColunas ** 2), quantidadeBombas)
    for botao in lista_botoes:
        botao.config(image = interrogacaoImagem, state = interface.NORMAL)


def iniciarGame():
    global janela, bombaImagem, bandeiraImagem, interrogacaoImagem, lblPontuacao
    janela = interface.Tk()
    janela.title('Campo Minado')
    janela.geometry('600x600')
    frameCampo = interface.Frame(janela)
    frameCampo.pack()

    framePontos = interface.Frame(janela)
    framePontos.pack()
    lblPontuacao = interface.Label(framePontos, text='Pontuação: 0')
    lblPontuacao.pack()

    caminhoBombaImagem = os.path.join(diretorio_atual, 'bomba.png')
    caminhoInterrogacaoImagem = os.path.join(diretorio_atual, 'interrogacao.png')
    caminhoBandeiraImagem = os.path.join(diretorio_atual, 'bandeira.png')

    bombaImagem = PhotoImage(file=caminhoBombaImagem)
    bandeiraImagem = PhotoImage(file=caminhoBandeiraImagem)
    interrogacaoImagem = PhotoImage(file=caminhoInterrogacaoImagem)
    idBotao = 0
    for linha in range(quantidadeLinhasColunas):
        for coluna in range(quantidadeLinhasColunas):
            btnGame = interface.Button(frameCampo, image=interrogacaoImagem, command=lambda id = idBotao: cliqueBotao(id))
            btnGame.grid(row=linha, column=coluna)
            lista_botoes.append(btnGame)
            idBotao = idBotao + 1

    janela.mainloop()

if __name__ =='__main__':
    iniciarGame()
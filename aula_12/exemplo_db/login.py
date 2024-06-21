import tkinter as interface
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect('bancoDados.db')
cursor = conn.cursor()

txtNome = None
txtUsuario = None
txtSenha = None
janela = None

def consultarUsuario(cursor):
    try:
        usuario = txtUsuario.get()
        senha = txtSenha.get()

        cursor.execute('SELECT * FROM Cliente WHERE usuario = ? and senha = ?', (usuario, senha))

        listaUsuario = cursor.fetchall()

        print(listaUsuario)

        if len(listaUsuario) > 0:
            messagebox.showinfo('Sucesso', 'Usuário encontrado')
        else:
            messagebox.showwarning('Falha', 'Usuário não encontrado')
    except Exception as err:
        messagebox.showerror('Erro', err)

def cadastrarLogin(cursor):
    try:
        nome = txtNome.get()
        usuario = txtUsuario.get()
        senha = txtSenha.get()

        cursor.execute('SELECT * FROM Cliente WHERE usuario = ?', (usuario,))

        listaUsuario = cursor.fetchall()
       
        if len(listaUsuario) > 0:
            messagebox.showwarning('Atenção', 'Este usuário já existe')
        else:
            cursor.execute('INSERT INTO Cliente (nome, usuario, senha) VALUES (?, ?, ?)', (nome, usuario, senha))
            conn.commit()

            messagebox.showinfo('Sucesso', 'Cadastrado com sucesso')

    except Exception as err:
        messagebox.showerror('Erro', err)

def atualizarLogin(cursor):
    try:
        nome = txtNome.get()
        usuario = txtUsuario.get()
        senha = txtSenha.get()

        cursor.execute('UPDATE Cliente SET nome = ?, senha = ? WHERE usuario = ?', (nome, senha, usuario))
        conn.commit()

        messagebox.showinfo('Sucesso', 'Usuário atualizado com sucesso')

    except Exception as err:
        messagebox.showerror('Erro', err)

def deletarLogin(cursor):
    try:
        usuario = txtUsuario.get()

        cursor.execute('DELETE FROM Login WHERE usuario = ?', (usuario,))
        conn.commit()
        messagebox.showinfo('Sucesso', 'Usuário deletado com sucesso')
    except Exception as err:
        messagebox.showerror('Erro', err)

def iniciarJanela():
    global janela, txtUsuario, txtSenha, txtNome
    janela = interface.Tk()
    janela.title('Teste')
    janela.geometry('400x400')

    lblNome = interface.Label(janela, text='Nome')
    lblNome.pack()

    txtNome = interface.Entry(janela)
    txtNome.pack()

    lblUsuario = interface.Label(janela, text='Usuario')
    lblUsuario.pack()
   
    txtUsuario = interface.Entry(janela)
    txtUsuario.pack()

    lblSenha = interface.Label(janela, text='Senha')
    lblSenha.pack()

    txtSenha = interface.Entry(janela)
    txtSenha.pack()

    btnLogin = interface.Button(janela, text='Login', command=lambda: consultarUsuario(cursor))
    btnLogin.pack()

    btnCadastrar = interface.Button(janela, text='Cadastrar', command=lambda: cadastrarLogin(cursor))
    btnCadastrar.pack()

    btnAtualizar = interface.Button(janela, text='Atualizar', command=lambda: atualizarLogin(cursor))
    btnAtualizar.pack()

    btnDeletar = interface.Button(janela, text='Deletar', command=lambda: deletarLogin(cursor))
    btnDeletar.pack()

    janela.mainloop()

if __name__ == '__main__':
    iniciarJanela()
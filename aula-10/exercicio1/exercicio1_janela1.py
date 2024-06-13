import tkinter as interface
from tkinter import messagebox
import exercicio1_janela2

janela = None
    

def iniciarJanela():
    global janela
    janela = interface.Tk()
    janela.geometry("400x200")
    janela.title("Login")

    frameForm = interface.Frame(janela)
    frameForm.pack()

    frameBotao = interface.Frame(janela)
    frameBotao.pack()

    # FORMULÁRIO
    # User
    lblUser = interface.Label(frameForm, text="Usuário:", font=10)
    lblUser.grid(row=0, column=0, padx=30, pady=10, sticky='w')

    txtUser = interface.Entry(frameForm, font=10)
    txtUser.grid(row=0, column=1, padx=30, pady=10)

    # Senha
    lblSenha = interface.Label(frameForm, text="Senha:", font=10)
    lblSenha.grid(row=2, column=0, padx=30, pady=10, sticky='w')

    txtSenha = interface.Entry(frameForm, show='*', font=15)
    txtSenha.grid(row=2, column=1, padx=30, pady=10)

    
    def login():
        user = txtUser.get()
        senha = txtSenha.get()

        if user == 'admin' or senha == '4321':
            janela.destroy()
            exercicio1_janela2.iniciarJanela()
        else:
            messagebox.showerror("Erro", "Usuário ou Senha incorretos")

             

    botaoEntrar = interface.Button(frameBotao, text="Entrar", command=login, font=15, width=8)
    botaoEntrar.pack(pady=10)

    janela.mainloop()


if __name__ == "__main__":
    iniciarJanela()
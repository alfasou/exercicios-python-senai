import tkinter as interface

def enviarForm():
    janela.destroy()

def iniciarJanela():
    global janela
    janela = interface.Tk()
    janela.geometry("500x350")
    janela.title("Janela 3")

    frameForm = interface.Frame(janela)
    frameForm.pack()

    frameBotao = interface.Frame(janela)
    frameBotao.pack()

    # FORMULÁRIO
    # Nome
    lblNome = interface.Label(frameForm, text="Nome:", font=15)
    lblNome.grid(row=0, column=0, padx=30, pady=10, sticky='w')

    txtNome = interface.Entry(frameForm, font=15)
    txtNome.grid(row=0, column=1, padx=30, pady=10)

    # Email
    lblEmail = interface.Label(frameForm, text="Email:", font=15)
    lblEmail.grid(row=1, column=0, padx=30, pady=10, sticky='w')

    txtEmail = interface.Entry(frameForm, font=15)
    txtEmail.grid(row=1, column=1, padx=30, pady=10)

    # CPF
    lblCPF = interface.Label(frameForm, text="CPF:", font=15)
    lblCPF.grid(row=2, column=0, padx=30, pady=10, sticky='w')

    txtCPF = interface.Entry(frameForm, font=15)
    txtCPF.grid(row=2, column=1, padx=30, pady=10)

    # Nome da Mãe
    lblMae = interface.Label(frameForm, text="Nome da Mãe:", font=15)
    lblMae.grid(row=3, column=0, padx=30, pady=10, sticky='w')

    txtMae = interface.Entry(frameForm, font=15)
    txtMae.grid(row=3, column=1, padx=30, pady=10)

    btnEnviar = interface.Button(janela, text="Enviar", command=enviarForm, font=15, width=8)
    btnEnviar.pack(pady=10)

    janela.mainloop()


if __name__ == "__main__":
    iniciarJanela()

senha = input('Adivinhe a senha: ')
senhaCorreta = 'python'

while senha != senhaCorreta:
    senha = input('Adivinhe a senha: ')
    if senha == senhaCorreta:
        print('\nAcertou! A senha é: "python"')
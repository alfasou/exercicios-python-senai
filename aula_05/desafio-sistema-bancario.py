conta = int(input('Digite o número da conta: '))
senha = int(input('Digite sua senha de 4 dígitos: '))
opcao = 1
saldo = 0
deposito = 0
saque = 0

while conta != 1234 or senha != 4321:
    print('\nUsuário ou senha incorretos')
    conta = int(input('\nDigite o número da conta: '))
    senha = int(input('Digite sua senha de 4 dígitos: '))
    
while opcao != 0:
    opcao = int(input('\nDigite uma das opções a seguir: \n1 - Verificar Saldo \n2 - Depositar dinheiro na conta \n3 - Retirar dinheiro da conta \n0 - Sair do sitema \n'))   
    if opcao == 1:
        print(f'\nSaldo: R${saldo:.2f}')
    elif opcao == 2:
        deposito = float(input('\nDigite o valor que deseja depositar: '))
        saldo += deposito
    elif opcao == 3:
        saque = float(input('\nDigite o valor que deseja retirar: '))
        saldo -= saque
    elif opcao == 0:
        print('\nOperação Finalizada')
        conta = int(input('\nDigite o número da conta: '))
        senha = int(input('Digite sua senha de 4 dígitos: '))
    else:
        print('\nOpção inválida')
        opcao = int(input('\nDigite uma das opções a seguir: \n1 - Verificar Saldo \n2 - Depositar dinheiro na conta \n3 - Retirar dinheiro da conta \n0 - Sair do sitema \n'))


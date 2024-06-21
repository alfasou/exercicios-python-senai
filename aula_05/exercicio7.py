operacao = int(input('Escolha uma operação matemática (1 - Adição, 2 - Subtração, 3 - Multiplicação ou 4 - Divisão): '))


while operacao != 0:
    numero1 = int(input('Escolha um número diferente de 0: '))
    numero2 = int(input('Escolha outro número diferente de 0: '))
    if operacao == 1:
        print(f'{numero1} + {numero2} = {int(numero1 + numero2)}')
        operacao = int(input('\nDeseja realizar outra operação ou 0 - Sair? '))
    elif operacao == 2:
        print(f'{numero1} - {numero2} = {int(numero1 - numero2)}')
        operacao = int(input('\nDeseja realizar outra operação ou 0 - Sair? '))
    elif operacao == 3:
        print(f'{numero1} x {numero2} = {int(numero1 * numero2)}')
        operacao = int(input('\nDeseja realizar outra operação ou 0 - Sair? '))
    elif operacao == 4:
        print(f'{numero1} / {numero2} = {int(numero1 / numero2)}')
        operacao = int(input('\nDeseja realizar outra operação ou 0 - Sair? '))
    else:
        print('operação não encontrada')


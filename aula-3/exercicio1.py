numero1 = int(input('Escreva um número: '))
numero2 = int(input('Escreva um novo número: '))
numero3 = int(input('Escreva mais um número: '))

if numero1 > numero2 and numero1 > numero3:
    print(f'O Primeiro Número ({numero1}) é o maior número')
elif numero2 > numero1 and numero2 > numero3:
    print(f'O Segundo Número ({numero2}) é o maior número')
elif numero3 > numero1 and numero3 > numero2:
    print(f'O Terceiro Número ({numero3}) é o maior número')
else:
    print(f'Não foi possível verificar qual dos três números ({numero1}, {numero2} ou {numero3}) é o maior')
numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))

if numero1 > numero2:
    while numero1 > numero2 + 1:
        numero1 -= 1
        print(numero1)
elif numero2 > numero1:
    while numero2 > numero1 + 1:
        numero2 -= 1
        print(numero2)
else:
    print('Os números são iguais')
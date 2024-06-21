numero = [int(input('Digite um número: '))]

while len(numero) != 5:
    numero.append(int(input('Digite mais um número: ')))

i = 0
soma = 0

while i != 5:
    soma += numero[i]
    i += 1

media = int(soma / 5)

print(f'\nA média dos números digitados é: {media}')
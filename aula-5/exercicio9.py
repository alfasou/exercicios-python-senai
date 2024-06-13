numeros = [int(input('Digite um número: '))]
pares = 0
i = 0

while len(numeros) < 10:
    numeros.append(int(input('Digite mais um número: ')))

while i < 10:
    if numeros[i] % 2 == 0:
        pares += 1
    i += 1

impares = 10 - pares

print(f'Dos números digitados, {pares} são pares e {impares} são ímpares')
    
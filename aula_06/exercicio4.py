palavra = input('Digite uma palavra: ')
i = len(palavra)
letrasPalavraInvertida = []

for letra in palavra:
    i -= 1
    letrasPalavraInvertida.append(palavra[i])

palavraInvertida = ''.join(letrasPalavraInvertida)

if palavraInvertida == palavra:
    print(f'A palavra {palavra} é um palíndromo')
else:
    print(f'A palavra {palavra} NÃO é um palíndromo')
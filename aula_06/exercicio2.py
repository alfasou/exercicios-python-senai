palavra = input('Digite uma palavra: ')
palavraInvertida = ''

for letra in range(len(palavra) -1, -1, -1):
    palavraInvertida += palavra[letra]

print(f'Sua palavra invertida é {palavraInvertida}')


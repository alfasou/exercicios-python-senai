import random

numero = random.randrange(1, 101)
palpite = int(input('Adivinhe o Número Secreto: '))
tentativa = 0
frase = ''

while numero != palpite:
    tentativa += 1
    if numero > palpite:
        print(f'\nO Número Secreto é maior que {palpite}')
        palpite = int(input('Tente de novo: '))
    else:
        print(f'\nO Número Secreto é menor que {palpite}')
        palpite = int(input('Tente de novo: '))

if tentativa > 1:
     frase = f'com {tentativa} tentativas'
else:
     frase = 'de PRIMEIRA!!'

if numero == palpite:
        print(f'\nParabéns! Você acertou o Número Secreto {frase}!')
palavra = input('Digite uma palavra qualquer: ').lower()
vogais = 'aeiou'
totalVogais = 0
i = 0

while i < len(palavra):
    if palavra[i] in vogais:
        totalVogais += 1
    i += 1

print(f'A palavra digitada possui {totalVogais} vogais')

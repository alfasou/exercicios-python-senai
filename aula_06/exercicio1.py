palavra = input('Digite uma palavra: ').lower()
numeroVogais = 0

for vogal in palavra:
    if vogal in 'aeiou':
        numeroVogais += 1

print(f'Em {palavra} há {numeroVogais} vogais')
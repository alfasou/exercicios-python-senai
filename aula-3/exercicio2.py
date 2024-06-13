preco1 = int(input('Escreva o preço do primeiro produto: '))
preco2 = int(input('Escreva o preço do segundo produto: '))
preco3 = int(input('Escreva o preço do terceiro produto: '))

if preco1 < preco2 and preco1 < preco3:
    print('Você deve comprar o primeiro produto')
elif preco2 < preco1 and preco2 < preco3:
    print('Você deve comprar o segundo produto')
elif preco3 < preco1 and preco3 < preco2:
    print('Você deve comprar o terceiro produto')
else:
    print('Não foi possível comparar os produtos.')
    

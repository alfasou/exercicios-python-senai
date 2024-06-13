id = int(input('Digite o ID do produto (1, 2, 3, 4 ou 5): '))

if id == 1:
    preco = 3999.99
    print(f'Produto: Playstation 5 \nValor: R${preco} \nValor com Desconto de 20%: R${(preco * 0.80):.2f}')
elif id == 2:
    preco = 4999.99
    print(f'Produto: iPhone 15 \nValor: R${preco} \nValor com Desconto de 30%: R${(preco * 0.60):.2f}')
elif id == 3:
    preco = 899.99
    print(f'Produto: Monitor Gamer \nValor: R${preco} \nValor com Desconto de 15%: R${(preco * 0.85):.2f}')
elif id == 4:
    preco = 2989.99
    print(f'Produto: Notebook Asus \nValor: R${preco} \nValor com Desconto de 10%: R${(preco * 0.90):.2f}')
elif id == 5:
    preco = 89.99
    print(f'Produto: Mouse Gamer \nValor: R${preco} \nValor com Desconto de 5%: R${(preco * 0.95):.2f}')
else:
    print(f'O ID {id} não foi encontrado.')
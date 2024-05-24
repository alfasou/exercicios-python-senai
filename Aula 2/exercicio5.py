id = int(input('Digite o ID do produto (1, 2, 3, 4 ou 5): '))

if id == 1:
    valor1 = 3999.99
    print(f'Produto: Playstation 5 \nValor: R${valor1} \nValor com Desconto de 20%: R${(valor1 * 0.80):.2f}')
elif id == 2:
    valor2 = 4999.99
    print(f'Produto: iPhone 15 \nValor: R${valor2} \nValor com Desconto de 30%: R${(valor2 * 0.60):.2f}')
elif id == 3:
    valor3 = 899.99
    print(f'Produto: Monitor Gamer \nValor: R${valor3} \nValor com Desconto de 15%: R${(valor3 * 0.85):.2f}')
elif id == 4:
    valor4 = 2989.99
    print(f'Produto: Notebook Asus \nValor: R${valor4} \nValor com Desconto de 10%: R${(valor4 * 0.90):.2f}')
elif id == 5:
    valor5 = 89.99
    print(f'Produto: Mouse Gamer \nValor: R${valor5} \nValor com Desconto de 5%: R${(valor5 * 0.95):.2f}')
else:
    print(f'O ID {id} não foi encontrado.')
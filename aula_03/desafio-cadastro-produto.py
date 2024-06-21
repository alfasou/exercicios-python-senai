nome = input('Escreva o nome do produto: ')
categoria = input('Escreva a categoria do produto: ')
precoCusto = int(input('Escreva o preço de custo do produto: '))

if categoria == 'Smartphone':
    precoVenda = precoCusto * 1.15
elif categoria == 'VideoGame':
    precoVenda = precoCusto * 1.2
elif categoria == 'Informática':
    precoVenda = precoCusto * 1.3
else:
    print('Categoria não encontrada.')
    

print(f'O preço de venda do Produto cadastrado é: R${precoVenda:.2f}')
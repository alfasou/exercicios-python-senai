idade = int(input('Digite a sua idade: '))
cnh = input('Você possui uma CNH válida? (S/N): ')

if idade >= 18 and cnh == 'S':
    print('Parabéns! Você pode dirigir!')
else:
    print('Que pena! Você não pode dirigir.')


mulheres = []
homens = []

for i in range(3):
    nomeMulher = input(f'Digite o nome da {i+1}ª uma mulher: ')
    nomeHomem = input(f'Digite o nome do {i+1}º homem: ')
    mulheres.append(nomeMulher)
    homens.append(nomeHomem)

print(f'\n\n')

for i in range(3):
    print(f'Dupla {i+1}: {mulheres[i]} e {homens[i]}')
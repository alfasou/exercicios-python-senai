pessoas = int(input('Quantas pessoas votarão na final? '))
votosNo1 = 0
votosNo2 = 0
votosNo3 = 0
pessoasVotaram = 0

while pessoasVotaram < pessoas:
    voto = int(input('Digite o número do participante no qual deseja votar (1, 2 ou 3): '))
    pessoasVotaram += 1
             
    if voto == 1:
        votosNo1 += 1
    elif voto == 2:
        votosNo2 += 1
    elif voto == 3:
        votosNo3 += 1

        
        
print(f'\nO participante número 1 recebeu {votosNo1} votos \nO participante número 2 recebeu {votosNo2} votos \nO participante número 3 recebeu {votosNo3} votos')
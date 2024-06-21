peixe = int(input('Escreva o peso total dos peixes em quilos: '))

if peixe > 50:
    excedente = peixe - 50
    multa = excedente * 4
    print(f'O peso excedente é de {excedente} e você deve parar R${multa:.2f} de multa')
else:
    print('O peso está dentro do regulamento.')
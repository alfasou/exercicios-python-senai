peso = float(input('Digite o seu peso em quilos: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / (altura **2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso Normal')
elif imc > 24.9 and imc < 29.9:
    print('Sobrepeso')
else:
    print('Obesidade')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura em centímetros: '))
imc = peso / (altura **2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso Normal')
elif imc >= 25 and imc < 29.9:
    print('Sobrepeso')
else:
    print('Obesidade')
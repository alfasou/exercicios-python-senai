salario = int(input('Escreva o salário do funcionário: '))

if salario >= 280:
    salarioAumento = salario * 1.2
    percentual = 20
    aumento = salario * .2
elif 700 >= salario > 280:
    salarioAumento = salario * 1.15
    percentual = 15
    aumento = salario * .15
elif 1500 > salario > 700:
    salarioAumento = salario * 1.1
    percentual = 10
    aumento = salario * .1
else:
    salarioAumento = salario * 1.05
    percentual = 5
    aumento = salario * .05


print(f'O salário anterior era R${salario:.2f}, o percentual de aumento é de {percentual}%, o valor do aumento foi de R${aumento:.2f} e o salário após o aumento ficou: R${salarioAumento:.2f}')
hora = int(input('Quantas horas você trabalha? '))
valorHora = int(input('Quanto você ganha por hora? '))
salarioBruto = hora * valorHora
ir = salarioBruto * .05
inss = salarioBruto * .10
fgts = salarioBruto * .11
descontos = ir + inss
salarioLiquido = salarioBruto - descontos

print(f'\nSalário Bruto: R${salarioBruto:.2f} \n(-) IR (5%): R${ir:.2f} \n(-) INSS (10%): R${inss:.2f} \nFGTS (11%): R${fgts:.2f} \nDesconto Total: R${descontos:.2f} \nSalário Líquido: R${salarioLiquido:.2f}')
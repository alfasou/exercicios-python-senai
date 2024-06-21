numero = int(input('Digite um número: '))
numeroPar = 0

while numeroPar < numero:
    numeroPar += 1
    if numeroPar % 2 == 0:
        print(numeroPar)
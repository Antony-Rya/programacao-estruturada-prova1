def q1():
    divisiveis = 0
    numero = int(input(""))
    for num in range(1, numero + 1):
        if numero % num == 0 and num % 3 == 0:
            divisiveis += 1
    if divisiveis == 0:
        print("O número não possui divisores multiplos de 3")
    else:
        print("Quantidade de divisores divisiveis por 3:", divisiveis)

def q2():
    pass

def q3():
    pass

def q4():
    pass

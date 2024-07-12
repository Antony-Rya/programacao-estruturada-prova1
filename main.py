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
    soma = 0
    menor = int(input(""))
    maior = int(input(""))
    if menor > maior:
        menor, maior = maior, menor
    for i in range(menor, maior + 1):
        if i > 0:
            soma += i
    print(soma)

def q3():
    servidores = int(input("Número de servidores: "))
    banco = int(input("Unidades de capacidade do banco de dados: "))
    armazenamento = int(input("Armazenamento de dados (em GB): "))
    transferencia = int(input("Transferência de dados de entrada e saída (em GB): "))
    Pservidores = servidores * 500
    Pbanco = banco * 100
    Parmazenamento = 
    Ptransf = transferencia * 0.10
    

def q4():
    pass

def somar():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 + num2
    print("Resultado:", resultado)

while True:
    somar()
    continuar = input("Deseja continuar? (S/N) ")
    if continuar.upper == "N":
        break
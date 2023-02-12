num1 = int(input("Digite um número maior que 1: "))
if num1 <= 1:
    print("O número deve ser maior que 1.")
else:
    for i in range(1, num1+1):
        print(i)
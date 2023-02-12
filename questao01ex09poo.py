salario = float(input("Digite o salário: "))

percentual_aumento = 0
valor_aumento = 0

if salario <= 280:
    percentual_aumento = 20
    valor_aumento = salario*0.2
elif salario > 280 and salario <= 700:
    percentual_aumento = 15
    valor_aumento = salario*0.15
elif salario > 700 and salario <= 1500:
    percentual_aumento = 10
    valor_aumento = 0.1
else: 
    percentual_aumento = 5
    valor_aumento = salario*0.05

novo_salario = salario + valor_aumento

print("Salário antes do reajuste: R$ %.2f" % salario)
print("Percentual de aumento aplicado: %d%%" % percentual_aumento)
print("Valor do aumento: R$ %.2f" % valor_aumento)
print("Novo salário: %.2f" % novo_salario) 
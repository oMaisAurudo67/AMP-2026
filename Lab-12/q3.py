num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

diferenca = num1 - num2

if diferenca < 0:
    diferenca = diferenca * -1

print("A diferenca absoluta entre os numeros e:", diferenca)
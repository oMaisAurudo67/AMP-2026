N = int(input("Quantos números quer digitar?"))
contador = 1
impares = 0

while contador <= N:
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        impares += 1
    contador += 1
print(f"Quantidade de ímpares entre 1 e {N}: {impares}")
#O contador nunca aumentava, entao o while nao funcionava e ficava infinito

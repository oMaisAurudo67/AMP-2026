import random

segredo = str(random.randint(100, 999))

for chance in range(1, 11):
    print( chance)

    palpite = input("Palpite: ")

    saida = ""

    for i in range(3):
        if palpite[i] == segredo[i]:
            saida += "+"
        elif palpite[i] in segredo:
            saida += "!"
        else:
            saida += "_"

    print("Saída:", saida)

    if saida == "+++":
        print("Parabens, Voce acertou")
        break
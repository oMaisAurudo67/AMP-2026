import random

p1 = 0
p2 = 0
rodada = 1

while p1 < 50 and p2 < 50:
    print(rodada)

    a = int(input("Jogador 1, seu palpite: "))
    b = int(input("Jogador 2, seu palpite: "))

    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)

    soma = d1 + d2

    print("Dado 1:", d1)
    print("Dado 2:", d2)
    print("Soma:", soma)

    e1 = abs(soma - a)
    e2 = abs(soma - b)

    if e1 < e2:
        p1 += 5
        print("Jogador 1 ganhou a rodada!")
    elif e2 < e1:
        p2 += 5
        print("Jogador 2 ganhou a rodada!")
    else:
        p1 += 2
        p2 += 2
        print("Empate")

    print("Placar:", p1, "x", p2)
    rodada += 1

if p1 >= 50:
    print("Jogador 1 venceu")
else:
    print("Jogador 2 venceu")
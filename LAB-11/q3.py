import random
import time

while True:
    op = input("Deseja fazer uma pergunta? (sim/não) ")

    if op.lower() == "não" or op.lower() == "nao":
        break

    pergunta = input("Faça sua pergunta: ")

    print("Deixa eu pensar...")
    time.sleep(2)

    print("Estou quase...")
    time.sleep(2)

    print("Eu tenho uma resposta")
    time.sleep(2)

    if random.randint(1, 10) <= 5:
        print("SIM")
    else:
        print("NAO")
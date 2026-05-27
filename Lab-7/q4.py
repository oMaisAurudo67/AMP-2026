import random
chances = 5
numero_secreto = (random.randint(1, 10))
while chances > 0: 
    numero = int(input(f"é o número certo? Você tem {chances} chances: "))
    chances -= 1
    if numero == 7:
        print("Você acertou o número, parabens")
        break
# eu copiei o codigo da questao passada e alterei os valores e o nome das variaveis para dar certo


while True:
    r = input("Você quer saber como manter uma pessoa ingenua ocupada por horas? S/N ")

    if r in ["s", "S", "sim", "SIM"]:
        continue
    elif r in ["n", "N", "nao", "NAO"]:
        print("Obrigado")
        break
    else:
        print("Resposta errada")
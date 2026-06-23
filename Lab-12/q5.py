import random
import time

n = random.randint(2, 10)
time.sleep(n)
print("agora!")
tempo0 = time.time()
input()
tempo1 = time.time()
print("Voce levou", tempo1 - tempo0, "segundos para responder.")
import random
import time

n = random.randint(0, 10)

for i in range(n):
    print(f"Volta {i + 1}: Mais uma volta!")
    time.sleep(1)
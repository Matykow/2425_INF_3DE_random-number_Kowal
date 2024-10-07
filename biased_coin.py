import random

def flip_biased_coin(p):
    return "Head" if random.random() < p else "Tails"
    pass

# Otestování funkce
print(flip_biased_coin(0.7))  # Simulace hodu s 70% šancí na výhru

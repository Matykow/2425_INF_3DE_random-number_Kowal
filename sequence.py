import random

def generate_sequence(n):
    for _ in range(n):
        print(random.randint(1, 1000))
    pass

# Otestování funkce
generate_sequence(10)  # Vygeneruje 10 náhodných čísel

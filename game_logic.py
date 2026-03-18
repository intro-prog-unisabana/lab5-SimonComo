from secret_number import *
from response import *

seed = int(input("Enter a seed number:\n"))
seed_secret_numbers(seed)

secret = generate_secret_number()

intentos = 0

while True:
    guess = int(input("What is your guess:\n"))
    intentos += 1

    mensaje, correcto = input_response(secret, guess)
    print(mensaje)

    if correcto:
        print(f"It took you {intentos} tries!")
        break
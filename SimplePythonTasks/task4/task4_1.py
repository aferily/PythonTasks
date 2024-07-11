import random

secret = random.randint(1, 10) 
print(f"secret: {secret}")

guess = random.randint(1, 10)
print(f"guess: {guess}")

if guess > secret:
    print("to high")
elif guess < secret:
    print("to low")
else:
    print("just right")

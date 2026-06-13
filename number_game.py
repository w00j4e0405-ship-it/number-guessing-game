import random

number = random.randint(1, 100)

print("Guess a number between 1 and 100!")

while True:
    guess = int(input("Enter a number: "))

    if guess < number:
        print("Try a higher number!")
    elif guess > number:
        print("Try a lower number!")
    else:
        print("correct!")
        break

    

 
    

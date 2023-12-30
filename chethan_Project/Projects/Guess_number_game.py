import random

guessing_number = random.randrange(1,20)

print("Well come to Guess number game")
number_of_guess = 1
total_number_of_guess = 8

while (number_of_guess < total_number_of_guess):
    try:
            input_guess = int(input("Enter the number: "))

            if guessing_number > input_guess:
                print("Please enter grater number \n Try again")
            elif guessing_number < input_guess:
                print("Please enter lessar number \n Try again")
            if guessing_number == input_guess:
                print("You are gussed correct")
                print("You won")
                print(number_of_guess, "no of guessess took to finish")
                break

            print((total_number_of_guess - number_of_guess), "no of guessess left")
            number_of_guess = number_of_guess + 1

            print(number_of_guess >= total_number_of_guess, "Game over")

    except Exception as e:
        print(f"Please enter the numbers only {e}")

print("Thank you for your participation ")

































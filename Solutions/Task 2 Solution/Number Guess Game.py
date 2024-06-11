import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    while True:
        try:
            user_guess = int(input("Guess the secret number (between 1 and 100): "))
            if user_guess == secret_number:
                print("Congratulations! You guessed it correctly.")
                break
            elif user_guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    guess_the_number()

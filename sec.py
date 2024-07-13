import random

def guess_the_number():
    number_to_guess = random.randint(0, 12)
    attempts = 0
    print("Welcome to Guess the Number Game!")
    print("I have selected a number between 0 and 99. Try to guess it!")
    
    while True:
        user_guess = input("Enter your guess: ")
        attempts += 1
        
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You have guessed the right number {number_to_guess} correctly in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()

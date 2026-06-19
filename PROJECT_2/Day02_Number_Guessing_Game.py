from random import randint

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 1000.")
    
    # Generate a random number between 1 and 1000
    secret_number = randint(1, 1000)
    attempts = 0
    
    while True:
        # Get the user's guess
        guess = input("Enter your guess (or type 'exit' to quit): ")
        
        # Check if the user wants to exit
        if guess.lower() == 'exit':
            print(f"The secret number was {secret_number}. Thanks for playing!")
            break
        
        # Validate the input
        if not guess.isdigit():
            print("Invalid input! Please enter a number between 1 and 1000.")
            continue
        
        guess = int(guess)
        
        # Check if the guess is within the valid range
        if guess < 1 or guess > 1000:
            print("Please guess a number between 1 and 1000.")
            continue
        
        attempts += 1
        
        # Check the user's guess against the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()
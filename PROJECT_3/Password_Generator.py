from random import randint

def generate_password(length):
    """Generate a random password of specified length."""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(characters[randint(0, len(characters) - 1)] for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        # --- STEP 1: GET PASSWORD LENGTH ---
        try:
            length = int(input("Enter the desired password length (or type '0' to exit): "))
            if length == 0:
                print("Thank you for using the Password Generator. Goodbye!")
                break  # Exit the loop if user enters 0
            elif length < 0:
                print("Please enter a positive integer for the password length.")
                continue  # Skip to the next iteration if input is negative
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue  # Skip to the next iteration if input is not an integer

        # --- STEP 2: GENERATE PASSWORD ---
        password = generate_password(length)
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
import secrets
import string

def generate_password(length):
    password = "".join(secrets.choice(string.ascii_letters + string.digits+ string.punctuation) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        # --- STEP 1: GET PASSWORD LENGTH ---
        try:
            length = int(input("Enter the desired password length (or type 'greater then 8' to exit): "))
            if length < 8:
                print("Please enter a length greater than or equal to 8.")
                continue  # Skip to the next iteration if input is less than 8
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue  # Skip to the next iteration if input is not an integer

        # --- STEP 2: GENERATE PASSWORD ---
        password = generate_password(length)
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
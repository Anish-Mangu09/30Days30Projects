print("Welcome to your Day 1 Calculator!")

while True:
    # --- STEP 1: DISPLAY MENU ---
    print("\n--- Menu ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit Program")

    # Get the user's choice
    choice = input("Enter your choice (1-5): ")

    # --- STEP 2: CHECK FOR EXIT ---
    if choice == "5":
        print("Thank you for using the calculator. Goodbye!")
        break  # This exits the while loop immediately

    # Validate choice before asking for numbers
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Please select a number from 1 to 5.")
        continue  # Skips the rest of the loop and starts over

    # --- STEP 3: GET NUMBERS ---
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # --- STEP 4: CALCULATE & OUTPUT ---
    if choice == "1":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")

    elif choice == "2":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")

    elif choice == "3":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")

    elif choice == "4":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
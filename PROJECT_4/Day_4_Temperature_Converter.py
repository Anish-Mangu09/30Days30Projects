# We don't have to import anything for this project, but we will be using the built in function "input" to get user input and "print" to display output.
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    print("Welcome to the Temperature Converter!")

    while True:
        # --- STEP 1: GET USER CHOICE ---
        choice = input("Type 'C' to convert Celsius to Fahrenheit, 'F' to convert Fahrenheit to Celsius, or 'Q' to quit: ").upper()

        if choice == 'Q':
            print("Thank you for using the Temperature Converter. Goodbye!")
            break  # Exit the loop if user chooses to quit
        elif choice not in ['C', 'F']:
            print("Invalid choice! Please enter 'C', 'F', or 'Q'.")
            continue  # Skip to the next iteration if input is invalid

        # --- STEP 2: GET TEMPERATURE VALUE ---
        try:
            temp_value = float(input("Enter the temperature value you want to convert: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue  # Skip to the next iteration if input is not a number

        # --- STEP 3: PERFORM CONVERSION ---
        if choice == 'C':
            converted_temp = celsius_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is equal to {converted_temp:.2f}°F.")
            
            if 97.0 <= converted_temp <= 99.0:
                print("The converted temperature is in the normal human body temperature range.")
            else:
                print("The converted temperature is not in the normal human body temperature range. Please consult a doctor for recommendations.")
        else:
            converted_temp = fahrenheit_to_celsius(temp_value)
            print(f"{temp_value}°F is equal to {converted_temp:.2f}°C.")
            
            if 36.1 <= converted_temp <= 37.2:
                print("The converted temperature is in the normal human body temperature range.")
            else:
                print("The converted temperature is not in the normal human body temperature range. Please consult a doctor for recommendations.")

if __name__ == "__main__":
    main()

from BMI import calculate_bmi  # Updated function name to match the previous example

def main():
    print("Welcome to the BMI Calculator! Please enter your height and weight when prompted.\n")
    
    try:
        Feet = int(input("Enter your height (Feet): "))
        Inches = int(input("Enter your height (Inches): "))
        Weight = float(input("Enter your weight (LBS): "))

        bmi, category = calculate_bmi(Feet, Inches, Weight)
        print(f"\nYour BMI is: {bmi}")
        print(f"Category: {category}")

    except ValueError:
        print("\nInvalid input. Please enter numeric values only.")

if __name__ == "__main__":
    main()

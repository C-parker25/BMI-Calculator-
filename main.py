from BMI import Calculate_BMI
def main():
    print("Welcome to the BMI Calculator PLease enter your height and weight when prompted")
    Feet = int(input("Please enter your height(Feet):  "))
    Inches = int(input("Please enter your height(Inches):  "))
    Weight = float(input("Please enter your weight(LBS):  "))

    BMI, Category = Calculate_BMI(Feet, Inches, Weight)
    print(f"BMI: {BMI}, Category: {Category}")


if __name__ == "__main__":
        main()
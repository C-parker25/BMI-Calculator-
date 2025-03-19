def calculate_bmi(Feet, Inches, Weight):
    if not isinstance(Feet, (int, float)) or not isinstance(Inches, (int, float)) or not isinstance(Weight, (int, float)):
        raise ValueError("Feet, Inches, and Weight must be numeric values.")

    Height_Inches = (Feet * 12) + Inches

    if Height_Inches <= 0:
        raise ValueError("Height must be greater than zero.")

    BMI = round((Weight / (Height_Inches ** 2)) * 703, 1)

    if BMI < 18.5:
        Category = "Underweight"
    elif BMI < 25:
        Category = "Normal Weight"
    elif BMI < 30:
        Category = "Overweight"
    else:
        Category = "Obese"

    return BMI, Category

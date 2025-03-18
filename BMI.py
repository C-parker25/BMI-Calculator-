def Calculate_BMI(Feet, Inches, Weight):
    height_Inches = (Feet * 12) + Inches
    BMI = (Weight /(height_Inches ** 2)) * 703
    BMI = round(BMI, 1)

    if BMI < 18.5:
        category = "Underweight"
    elif BMI < 25:
        category = "Normal Weight"
    elif BMI < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return BMI, category
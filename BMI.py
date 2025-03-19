def calculate_bmi(Feet, Inches, Weight):
    def _bmi_category(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal Weight"
        elif bmi < 30:
            return "Overweight"
        return "Obese"

    height_inches = (Feet * 12) + Inches
    bmi = round((Weight / (height_inches ** 2)) * 703, 1)
    
    return bmi, _bmi_category(bmi)

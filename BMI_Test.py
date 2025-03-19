import unittest
from BMI import calculate_bmi

class TestBMICalculator(unittest.TestCase):

    def test_underweight(self):
        self.assertEqual(calculate_bmi(5, 6, 100), (16.1, "Underweight"))
        self.assertEqual(calculate_bmi(6, 0, 130), (17.6, "Underweight"))

    def test_normal_weight(self):
        self.assertEqual(calculate_bmi(5, 8, 150), (22.8, "Normal Weight"))
        self.assertEqual(calculate_bmi(6, 2, 180), (23.1, "Normal Weight"))

    def test_overweight(self):
        self.assertEqual(calculate_bmi(5, 9, 180), (26.6, "Overweight"))
        self.assertEqual(calculate_bmi(6, 1, 210), (27.7, "Overweight"))

    def test_obese(self):
        self.assertEqual(calculate_bmi(5, 5, 200), (33.3, "Obese"))
        self.assertEqual(calculate_bmi(6, 4, 250), (30.4, "Obese"))

    def test_boundary_cases(self):
        self.assertEqual(calculate_bmi(5, 7, 121), (18.9, "Normal Weight"))

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(0, 0, 150)

    def test_extreme_values(self):
        self.assertEqual(calculate_bmi(7, 0, 300), (29.9, "Overweight"))

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate_bmi("five", 7, 150)  # Non-numeric feet
        with self.assertRaises(ValueError):
            calculate_bmi(5, "seven", 150)  # Non-numeric inches
        with self.assertRaises(ValueError):
            calculate_bmi(5, 7, "one fifty")  # Non-numeric weight

if __name__ == '__main__':
    unittest.main()

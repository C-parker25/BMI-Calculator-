import unittest
from BMI import Calculate_BMI

class TestBMICalculator(unittest.TestCase):

    def test_underweight(self):
        """Test BMI values in the Underweight range (<18.5)"""
        self.assertEqual(Calculate_BMI(5, 6, 100), (16.1, "Underweight"))
        self.assertEqual(Calculate_BMI(6, 0, 130), (17.6, "Underweight"))

    def test_normal_weight(self):
        """Test BMI values in the Normal Weight range (18.5 - 24.9)"""
        self.assertEqual(Calculate_BMI(5, 8, 150), (22.8, "Normal Weight"))
        self.assertEqual(Calculate_BMI(6, 2, 180), (23.1, "Normal Weight"))

    def test_overweight(self):
        """Test BMI values in the Overweight range (25 - 29.9)"""
        self.assertEqual(Calculate_BMI(5, 9, 180), (26.6, "Overweight"))
        self.assertEqual(Calculate_BMI(6, 1, 210), (27.7, "Overweight"))

    def test_obese(self):
        """Test BMI values in the Obese range (>=30)"""
        self.assertEqual(Calculate_BMI(5, 5, 200), (33.3, "Obese"))
        self.assertEqual(Calculate_BMI(6, 4, 250), (30.4, "Obese"))

    def test_boundary_cases(self):
        """Test boundary cases at category transitions"""
        self.assertEqual(Calculate_BMI(5, 7, 121), (18.9, "Normal Weight"))

    def test_zero_height(self):
        """Test handling of zero height input"""
        with self.assertRaises(ZeroDivisionError):
            Calculate_BMI(0, 0, 150)

    def test_extreme_values(self):
        """Test very high or low height/weight values"""
        self.assertEqual(Calculate_BMI(7, 0, 300), (29.9, "Overweight"))

if __name__ == '__main__':
    unittest.main()

import unittest
from triangle_func import IncorrectTriangleSides, get_triangle_type

class TestTriangleFunc(unittest.TestCase):
    # Класс тестов для функции get_triangle_type

    def test_equilateral(self):
        # Проверка для равностороннего треугольника
        self.assertEqual(get_triangle_type(1, 1, 1), "равносторонний")

    def test_isosceles(self):
        # Проверка для равнобедренного треугольника
        self.assertEqual(get_triangle_type(3, 4, 4), "равнобедренный")

    def test_nonequilateral(self):
        # Проверка для неравностороннего треугольника
        self.assertEqual(get_triangle_type(3, 4, 5), "неравносторонний")

    def test_invalid_sides_1(self):
        # Проверка для исключения при некорректных сторонах
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 1, 1)

    def test_invalid_sides_2(self):
        # Проверка для исключения при отрицательной стороне
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, -4, 5)

    def test_invalid_sides_3(self):
        # Проверка для исключения при невозможности образования треугольника
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, 4, 10)

class TestSpecificCases(unittest.TestCase):
    # Класс тестов для конкретных случаев треугольников

    def test_equilateral_case(self):
        # Проверка конкретного равностороннего треугольника
        self.assertEqual(get_triangle_type(2, 2, 2), "равносторонний")

    def test_isosceles_case(self):
        # Проверка конкретного равнобедренного треугольника
        self.assertEqual(get_triangle_type(5, 4, 5), "равнобедренный")

    def test_nonequilateral_case(self):
        # Проверка конкретного неравностороннего треугольника
        self.assertEqual(get_triangle_type(4, 6, 7), "неравносторонний")

    def test_invalid_sides_4(self):
        # Проверка для дополнительного исключения при некорректных сторонах
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 10)

if __name__ == "__main__":
    unittest.main()


from triangle_func import IncorrectTriangleSides


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        # Конструктор класса, проверяющий корректность сторон треугольника
        if not (a > 0 and b > 0 and c > 0):
            raise IncorrectTriangleSides("Стороны треугольника должны быть положительными")
        if a + b <= c or a + c <= b or b + c <= a:
            raise IncorrectTriangleSides("Стороны треугольника не могут образовывать треугольник")
        
        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self) -> str:
        # Метод определения типа треугольника (равносторонний, равнобедренный, неравносторонний)
        if self.a == self.b == self.c:
            return "равносторонний"
        elif self.a == self.b or self.b == self.c or self.c == self.a:
            return "равнобедренный"
        else:
            return "неравносторонний"

    def per(self) -> float:
        # Метод вычисления периметра треугольника
        return self.a + self.b + self.c


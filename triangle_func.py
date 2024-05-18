class IncorrectTriangleSides(Exception):
    # Определение пользовательского исключения IncorrectTriangleSides
    pass

def get_triangle_type(a: float, b: float, c: float) -> str:
    # Функция для определения типа треугольника по длинам его сторон
    if not (a > 0 and b > 0 and c > 0):
        raise IncorrectTriangleSides("Стороны должны быть положительными")
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides("Невозможно образовать треугольник с данными сторонами")
    
    if a == b == c:
        return "равносторонний"
    elif a == b or b == c or c == a:
        return "равнобедренный"
    else:
        return "неравносторонний"

 

 

 

 

 

 

 

 

 

 

 
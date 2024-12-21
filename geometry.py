import math
def circumcircle_radius(a, b, c):
    """Обчислення радіуса описаного кола навколо трикутника за довжинами сторін"""
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    radius = (a * b * c) / (4 * area)
    return radius

def incircle_radius(a, b, c):
    """Обчислення радіуса вписаного кола в трикутник за довжинами сторін"""
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    radius = area / s
    return radius
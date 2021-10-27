from math import pi, sqrt

if __name__ == "__main__":
    s1 = float(input())
    s2 = float(input())
    r_o = sqrt(s2 / pi)
    a = 2 * sqrt(S / sqrt(3))
    r = a * sqrt(3) / 6
    R = a * sqrt(3) / 3
    
    if r_o <= r:
        print("Да, окружность может вписываться в треугольник")
    else:
        print("Нет, окружность не может вписываться в треугольник")
        
    if r_o >= R:
        print("Да, треугольник может вписываться в окружность")
    else:
        print("Нет, треугольник не может вписываться в окружность")
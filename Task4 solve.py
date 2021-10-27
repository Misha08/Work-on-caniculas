a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
if D < 0:
    print('Действительных корней нет')
elif D == 0:
    x = -b / (2 * a)
    print('Уравнение имеет два действительных кореней', x ** 0.5, -(x ** 0.5))
else:
    t1 = (-b + D ** 0.5) / (2 * a)
    t2 = (-b - D ** 0.5) / (2 * a)
    possible_roots = list()
    roots = list()
    if t1 < 0:
        t1 = 'None'
    if t2 < 0:
        t2 = 'None'
    possible_roots.append(t1)
    possible_roots.append(t2)
    for i in possible_roots:
        if i != 'None':
            x = i ** 0.5
            roots.append(x)
            roots.append(-x)
        # print(roots)

    print('Уравнение имеет корени', *roots)
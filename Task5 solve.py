a, b, c = float(input()), float(input()), float(input())
x, y = float(input()), float(input())

yes_string = 'Кирпич влазеет в дырку'

if a <= x and b <= y:
    print(yes_string)
elif a <= y and b <= x:
    print(yes_string)
elif b <= x and c <= y:
    print(yes_string)
elif c <= x and b <= y:
    print(yes_string)
elif a <= x and c <= y:
    print(yes_string)
elif c <= x and a <= y:
    print(yes_string)
else:
    print('Кирпич не влазеет в дырку')
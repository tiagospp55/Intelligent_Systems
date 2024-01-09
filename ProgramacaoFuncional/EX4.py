import math

def f(x,y):
    return x + y

def g(y,z):
    return y + z

def h(f,g):
    return lambda x,y,z: f(x,y) + g(y,z)

def falinea7(f,lista):
    for x in lista:
        if f(x):
            return True
    return False

par = lambda x: x % 2 == 0 
print('par ', par(6), 'impar', par(7))

positive = lambda x: x > 0
print('positive ', positive(6), 'negative', positive(-7))

greater = lambda x, y: abs(x) > abs(y)
print('greater ', greater(7,6), 'smaller', greater(-7, 6))

polar = lambda x,y:  (math.hypot(x, y), math.degrees(math.atan2(y, x)))
print('polar', polar(1,2))

print('h:', h(f(1,2),g(1,2)))

lista = [0, 1, 2, 3, 4, 5]
alinea7 = lambda x: x > 8
print('aline7', falinea7(alinea7, lista)) 

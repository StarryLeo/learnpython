import math
def quadratic(a, b, c):
    t = b*b - 4*a*c
    if t<0:
        print('没有实数解')
    else:
        x1 = (-b + math.sqrt(t))/2*a
        x2 = (-b - math.sqrt(t))/2*a
        return x1, x2

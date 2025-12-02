import math
r = 6.5
a, b = map(float, input().split('x'))
d = 2 * r
dg = math.hypot(a, b)
if dg <= d:
    print("да")
else:
    print("нет")

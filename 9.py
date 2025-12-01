import math
x1, y1, r1 = map(float, input().split())
x2, y2, r2 = map(float, input().split())
d = math.hypot(x1 - x2, y1 - y2)

if d > r1 + r2:
    print("окружности лежат вне друг друга, не касаясь")
elif d == r1 + r2:
    print("окружности имеют внешнее касание")
elif abs(r1 - r2) < d < r1 + r2:
    print("окружности пересекаются")
elif d == abs(r1 - r2):
    print("окружности имеют внутреннее касание")
else:
    print("одна окружность лежит внутри другой, не касаясь")

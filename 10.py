x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
if x2 < x3 or x4 < x1 or y1 < y4 or y3 < y2:
    print("прямоугольники лежат вне друг друга, не касаясь")
elif x2 == x3 or x4 == x1 or y1 == y4 or y3 == y2:
    print("прямоугольники имеют касание")
elif (x1 < x3 and y1 > y3 and x2 > x4 and y2 < y4) or\(x3 < x1 and y3 > y1 and x4 > x2 and y4 < y2):
    print("один прямоугольник лежит внутри другого, не касаясь")
else:
    print("прямоугольники имеют пересечение")

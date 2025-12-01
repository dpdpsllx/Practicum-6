a = input()  
b = input()  
c1 = ord(a[0]) - ord('a') + 1
r1 = int(a[1])
c2 = ord(b[0]) - ord('a') + 1
r2 = int(b[1])
x = abs(c2 - c1)
y = abs(r2 - r1)
if (x == 2 and y == 1) or (x == 1 and y == 2):
    print("верно")
else:
    print("ошибка")

A, B = map(int, input().split())
C, D, E = map(int, input().split())
sides = [(C, D), (C, E), (D, E)]
for x, y in sides:
    if (x <= A and y <= B) or (x <= B and y <= A):
        print("да")
        break
    else:
        print("нет")
        break

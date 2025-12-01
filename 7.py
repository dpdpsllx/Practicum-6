n = int(input())
if (n % 5 == 0) or (n % 7 == 0) or (n >= 12 and (n - 12) % 5 == 0):
    print("да")
else:
    print("нет")

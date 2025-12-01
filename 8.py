n = int(input())
k = 1  
if n == 1:
    print(0)
else:
    for x in range(1, 200 + 1):
        a = x // 10
        b = x % 10
        if x < 10:
            k += 1
            if k == n:
                print(b)
                break
        else:
            k += 1
            if k == n:
                print(a)
                break
            k += 1
            if k == n:
                print(b)
                break

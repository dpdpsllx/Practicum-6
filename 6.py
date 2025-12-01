N, K, M = map(int, input().split())
total = N * 2
if total % K == 0:
    full = total // K
else:
    full = total // K + 1
time = full * M
print(time)

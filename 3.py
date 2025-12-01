N, M = map(int, input().split())
K = int(input())
if (K % N == 0 and K // N < M) or (K % M == 0 and K // M < N):
    print("успешно")
else:
    print("несуществимо")

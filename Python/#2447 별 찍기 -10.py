# 문제 출처: https://www.acmicpc.net/problem/2447
# 풀이: 2021.01.26

def check_star(X, Y, N):
    if N == 1:
        check[X][Y] = 1
        return
    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                check_star(X-N//3*i, Y-N//3*j, N//3)


N = int(input())
check = [[0 for x in range(N+1)] for y in range(N+1)]
check_star(N, N, N)

for i in range(1,N+1):
    for j in range(1, N+1):
        print("*", end="") if check[i][j] else print(" ", end="")
    print()
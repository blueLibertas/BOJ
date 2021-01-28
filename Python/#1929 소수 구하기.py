# 문제 출처: https://www.acmicpc.net/problem/1929
# 풀이: 2021.01.28

M, N = map(int, input().split())

End = N
prime = []
check = [True] * (End+1)

for i in range(2, End+1):
    if (check[i]):
        if i >= M:
            print(i)
        for j in range(End//i+1):
            check[i*j] = False
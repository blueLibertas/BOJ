# 문제 출처: https://www.acmicpc.net/problem/10872
# 풀이: 2021.01.30

def factorial(N):
    if N == 0 or N == 1:
        return 1
    return N*factorial(N-1)

N = int(input())
print(factorial(N))
# 문제 출처: https://www.acmicpc.net/problem/10870
# 풀이: 2021.01.26

"""주의! 첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다."""

def fibonacci(N):
    if N == 1 or N == 2:
        return 1
    if N == 0:
        return 0
    return fibonacci(N-1) + fibonacci(N-2)

print(fibonacci((int(input()))))
# 문제 출처: https://www.acmicpc.net/problem/10952
# 풀이: 2021.01.17

A, B = map(int, input().split())
while A != 0 and B != 0:
    print(A+B)
    A, B = map(int, input().split())

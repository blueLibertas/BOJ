# 문제 출처: https://www.acmicpc.net/problem/1330
# 풀이: 2021.01.16

A, B = map(int, input().split())
print(">" if A>B else "==" if A==B else "<")
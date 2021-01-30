# 문제 출처: https://www.acmicpc.net/problem/1085
# 풀이: 2021.01.30

X, Y, W, H = map(int, input().split())
print(min(X, Y, W-X, H-Y))
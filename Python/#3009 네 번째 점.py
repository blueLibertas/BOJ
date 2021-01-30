# 문제 출처: https://www.acmicpc.net/problem/3009
# 풀이: 2021.01.30

X = [-1,-1,-1]
Y = [-1,-1,-1]
X[0], Y[0] = map(int, input().split())
X[1], Y[1] = map(int, input().split())
X[2], Y[2] = map(int, input().split())
X.sort()
Y.sort()

print(X[2] if X[0]==X[1] else X[0], Y[2] if Y[0]==Y[1] else Y[0])

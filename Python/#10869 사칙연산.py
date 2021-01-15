# 문제 출처: https://www.acmicpc.net/problem/10869
# 풀이: 2021.01.15

A, B = map(int, input().split())
print("{}\n{}\n{}\n{}\n{}\n".format(A+B, A-B, A*B, A//B, A%B))
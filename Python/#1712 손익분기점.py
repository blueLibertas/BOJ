# 문제 출처: https://www.acmicpc.net/problem/1712
# 풀이: 2021.01.19

A, B, C = map(int, input().split())
print(-1 if C <= B else (A//(C-B)+1))
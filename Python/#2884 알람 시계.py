# 문제 출처: https://www.acmicpc.net/problem/2884
# 풀이: 2021.01.16

H, M = map(int, input().split())
total = (H*60 + M - 45) % 1440
print(total//60, total%60)
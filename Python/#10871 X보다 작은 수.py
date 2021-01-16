# 문제 출처: https://www.acmicpc.net/problem/10871
# 풀이: 2021.01.16

N, X = map(int, input().split())
for num in input().split():
    print(num+" " if int(num)<X else "", end="")
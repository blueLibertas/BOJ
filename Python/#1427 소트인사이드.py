# 문제 출처: https://www.acmicpc.net/problem/1427
# 풀이: 2021.02.12

N = [int(x) for x in input()]
N.sort(reverse=True)
for n in N:
    print(n, end="")
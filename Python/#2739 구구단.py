# 문제 출처: https://www.acmicpc.net/problem/2739
# 풀이: 2021.01.16

N = int(input())
for i in range(1, 10):
    print("{} * {} = {}".format(N, i, N*i))
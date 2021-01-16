# 문제 출처: https://www.acmicpc.net/problem/15552
# 풀이: 2021.01.16

import sys
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    print(sum(map(int, sys.stdin.readline().rstrip().split())))
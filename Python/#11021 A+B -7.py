# 문제 출처: https://www.acmicpc.net/problem/11021
# 풀이: 2021.01.16

T = int(input())
for i in range(T):
    print("Case #{}: {}".format(i+1, sum(map(int, input().split()))))
# 문제 출처: https://www.acmicpc.net/problem/11022
# 풀이: 2021.01.16

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i+1, A, B, A+B))
# 문제 출처: https://www.acmicpc.net/problem/7568
# 풀이: 2021.02.02

N = int(input())
weight_height = [[0,0,1] for i in range(N)]
for i in range(N):
    weight_height[i][0],weight_height[i][1] = map(int, input().split())

for i in range(N):
    for j in range(N):
        if i != j and weight_height[i][0] < weight_height[j][0] and weight_height[i][1] < weight_height[j][1]:
            weight_height[i][2] += 1

for i in range(N):
    print(weight_height[i][2], end=' ')
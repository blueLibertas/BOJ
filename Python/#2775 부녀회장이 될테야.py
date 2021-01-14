# 문제 출처: https://www.acmicpc.net/problem/2775
# 풀이: 2021.01.11

N = int(input())
for i in range(N):
    k = int(input())
    n = int(input())

    living = [[x for x in range(n+1)]]
    for floor in range(1, k+1):
        temp = [1, 1]
        for num in range(2, n+1):
            temp.append(sum(living[floor-1][1:num+1]))
        living.append(temp)
    print(living[k][n])
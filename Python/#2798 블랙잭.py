# 문제 출처: https://www.acmicpc.net/problem/2798
# 풀이: 2021.01.31

N, M = map(int, input().split())
cards = [int(x) for x in input().split()]
temp = 0

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        for k in range(N):
            if i==k or j==k:
                continue
            sum = cards[i]+cards[j]+cards[k]
            if sum>M:
                continue
            if sum > temp:
                temp = sum
print(temp)

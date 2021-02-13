# 문제 출처: https://www.acmicpc.net/problem/11047
# 풀이: 2021.02.13

N, cost = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))
count = 0

def how_many_coins(cost):
    global count
    for i in range(N-1, -1, -1):
        if cost >= coins[i]:
            temp = cost // coins[i]
            count += temp
            cost -= temp * coins[i]
            if cost == 0:
                return

how_many_coins(cost)
print(count)
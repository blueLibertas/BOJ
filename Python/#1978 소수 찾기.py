# 문제 출처: https://www.acmicpc.net/problem/1978
# 풀이: 2021.01.17

N = int(input())
given = set(map(int, input().split()))

prime = [x for x in range(2, 1001)]
for i in range(2, 501):
    for x in prime:
        if x*i in prime:
            prime.remove(x*i)

print(len(given&set(prime)))
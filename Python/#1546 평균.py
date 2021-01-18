# 문제 출처: https://www.acmicpc.net/problem/1546
# 풀이: 2021.01.18

N = int(input())
scores = list(map(int, input().split()))
print(sum(scores)/N/max(scores)*100)
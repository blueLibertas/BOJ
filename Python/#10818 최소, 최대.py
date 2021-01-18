# 문제 출처: https://www.acmicpc.net/problem/10818
# 풀이: 2021.01.18

N = int(input())
numbers = [int(x) for x in input().split()]
print(min(numbers), max(numbers))
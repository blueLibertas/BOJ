# 문제 출처: https://www.acmicpc.net/problem/2750
# 풀이: 2021.02.04

N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))

for i in range(N-1):
    for j in range(N-i-1):
        if numbers[j] > numbers[j+1]:
            temp = numbers[j+1]
            numbers[j+1] = numbers[j]
            numbers[j] = temp
    print(numbers)

for num in numbers:
    print(num)
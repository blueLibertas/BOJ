# 문제 출처: https://www.acmicpc.net/problem/2751
# 풀이: 2021.02.05

import sys

def sort_numbers(numbers):
    N, half = len(numbers), len(numbers)//2
    if N == 1:
        return numbers

    num1, num2 = sort_numbers(numbers[:half]), sort_numbers(numbers[half:])

    i = j = 0
    merged = []
    while i != len(num1) and j != len(num2):
        if  num1[i] <= num2[j]:
            merged.append(num1[i])
            i += 1
        else:
            merged.append(num2[j])
            j += 1
    merged += num1[i:]
    merged += num2[j:]

    return merged


N = int(sys.stdin.readline().rstrip())
input_numbers = []
for i in range(N):
    input_numbers.append(int((sys.stdin.readline().rstrip())))

final = sort_numbers(input_numbers)

print('\n'.join(map(str,final)))
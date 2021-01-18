# 문제 출처: https://www.acmicpc.net/problem/2562
# 풀이: 2021.01.18

max_index = -1
max_num = -1
for i in range(9):
    temp = int(input())
    if temp > max_num:
        max_num = temp
        max_index = i+1
print(max_num)
print(max_index)
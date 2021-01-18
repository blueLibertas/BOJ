# 문제 출처: https://www.acmicpc.net/problem/2577
# 풀이: 2021.01.18

ABC = str(int(input()) * int(input()) * int(input()))
count = [0 for x in range(10)]

for num in ABC:
    count[int(num)]+= 1

for counts in count:
    print(counts)

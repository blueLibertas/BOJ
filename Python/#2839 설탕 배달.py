# 문제 출처: https://www.acmicpc.net/problem/2839
# 풀이: 2021.01.21

def calculate(weight):
    if weight in [1,2,4,7]:
        return -1
    div = weight//5
    remainder = weight%5
    if remainder == 0:
        return div
    elif remainder == 1 or remainder == 3:
        return div+1
    else:
        return div+2

print(calculate(int(input())))



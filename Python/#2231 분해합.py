# 문제 출처: https://www.acmicpc.net/problem/2231
# 풀이: 2021.01.31

def find(N):
    l = len(N)
    start = max(int(N)-10*l, 1)
    for i in range(start, int(N)):
        if i+sum(int(x) for x in str(i)) == int(N):
            return i
    return 0

N = input()
print(find(N))

# 문제 출처: https://www.acmicpc.net/problem/11729
# 풀이: 2021.01.30

def hanoi(N, start, dest, middle):
    if N == 1:
        print(start, dest)
        return
    hanoi(N-1, start, middle, dest)
    print(start, dest)
    hanoi(N-1, middle, dest, start)

N = int(input())
print(2**N-1)
hanoi(N, 1, 3, 2)
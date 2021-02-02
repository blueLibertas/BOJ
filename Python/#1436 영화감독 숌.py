# 문제 출처: https://www.acmicpc.net/problem/1436
# 풀이: 2021.02.02

def find_nth_movie(N):
    i = 666
    nth = 1

    while nth != N:
        i += 1
        if '666' in str(i):
            nth += 1

    return i

N = int(input())
print(find_nth_movie(N))
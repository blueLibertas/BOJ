# 문제 출처: https://www.acmicpc.net/problem/2960
# 풀이: 2021.01.25

def nth_prime(until, nth):
    numbers = [x for x in range(2, until+1)]
    for i in range(2, until+1):
        if i not in numbers:
            continue
        nth -= 1
        if nth == 0:
            return i
        numbers.remove(i)

        for temp in range(2, until//i+1):
            if i*temp in numbers:
                numbers.remove(i*temp)
                nth -= 1
                if nth == 0:
                    return i*temp


N, K = map(int, input().split())
print(nth_prime(N, K))
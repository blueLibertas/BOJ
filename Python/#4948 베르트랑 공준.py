# 문제 출처: https://www.acmicpc.net/problem/4948
# 풀이: 2021.01.29

def Bertrand(N):
    count = 0
    for number in prime:
        if number > 2 * N:
            return count
        if number > N:
            count += 1
    return count

End = 123456 * 2
prime = []
check = [True] * (End+1)

for i in range(2, End+1):
    if (check[i]):
        prime.append(i)
        for j in range(End//i+1):
            check[i*j] = False

N = int(input())
while N!= 0:
    print(Bertrand(N))
    N = int(input())




# 문제 출처: https://www.acmicpc.net/problem/1110
# 풀이: 2021.01.17

def makeNewNum(number):
    return (number//10+number%10)%10+number%10*10

N = int(input())
new_Num = makeNewNum(N)
count = 1

while N != new_Num:
    new_Num = makeNewNum(new_Num)
    count += 1

print(count)
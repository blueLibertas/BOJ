# 문제 출처: https://www.acmicpc.net/problem/9498
# 풀이: 2021.01.16

A= int(input())
print("A" if A>=90 else "B" if A>=80 else "C" if A>=70 else "D" if A>= 60 else "F")


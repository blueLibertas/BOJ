# 문제 출처: https://www.acmicpc.net/problem/2753
# 풀이: 2021.01.16

A= int(input())
print(1 if (A%4==0 and A%100!=0) or A%400==0 else 0)
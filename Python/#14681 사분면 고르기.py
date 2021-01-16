# 문제 출처: https://www.acmicpc.net/problem/14681
# 풀이: 2021.01.16

A = int(input())
B = int(input())
print(1 if (A>0 and B>0) else 2 if (A<0 and B>0) else 3 if (A<0 and B<0) else 4)
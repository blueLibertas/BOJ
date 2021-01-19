# 문제 출처: https://www.acmicpc.net/problem/2908
# 풀이: 2021.01.19

A, B = input().split()
A_ = int(A[2]+A[1]+A[0])
B_ = int(B[2]+B[1]+B[0])
print(A_ if A_>B_ else B_)
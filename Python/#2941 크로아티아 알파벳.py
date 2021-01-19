# 문제 출처: https://www.acmicpc.net/problem/2941
# 풀이: 2021.01.19

word = input()
c_alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for item in c_alpha:
    word = word.replace(item, " ")
print(len(word))



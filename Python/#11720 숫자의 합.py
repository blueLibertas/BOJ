# 문제 출처: https://www.acmicpc.net/problem/11720
# 풀이: 2021.01.19

word = input()
a_ord = ord('a')
index = [-1 for x in range(26)]
for idx, letter in enumerate(word):
    if index[ord(letter)-a_ord] == -1:
        index[ord(letter)-a_ord] = idx
print(" ".join(map(str, index)))
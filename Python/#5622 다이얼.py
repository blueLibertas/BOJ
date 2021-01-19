# 문제 출처: https://www.acmicpc.net/problem/5622
# 풀이: 2021.01.19

call = input()
time_reference = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
time = 0
for letter in call:
    time += time_reference[ord(letter)-ord("A")]
print(time)



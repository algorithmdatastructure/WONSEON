import collections

s = [i for i in input()] # input list화

ss = dict()

L = list(range(97, 123)) # Ascii code

l = [chr(i) for i in L] # Ascii to alphabet

# Default Dictionary 설정
for i in l :
    ss.setdefault(i, 0)

# Input에 맞는 값들 투입.
for i in s :
    if i in ss.keys() :
        ss[i] += 1
# 결과 출력
print(*ss.values())

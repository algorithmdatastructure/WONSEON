# -*- coding: utf-8

n = int(input())
# ['8', 'fced'] -> ['8', ['f', 'c', 'e', 'd'] ]
s = []
for num in range(n):
    t = [i for i in input()]
    s.append(t)

# Ascii code로 바꿔서 diverse인지 확인하는 함수
def criti(x) :

    asc = [ord(i) for i in x] # alphabet to Ascii
    asc.sort()

    from collections import Counter # 모든 item count 할때.

    if len(x)-1 == sum([a-b for a, b in zip(asc[1:], asc[:-1])]) : # 정렬된 ascii에서 바로 앞과 차를 구해서 계산
        dup = Counter(asc)
        if len([i for i in dup.values() if i > 1]) == 0 : # 중복된 문자 걸러주는 부분
            return "Yes"
        else :
            return "No"
    else :
        return "No"

# 결과 출력 함수
for i in range(n) :
    if len(s[i]) == 1 :
        print("Yes")
    else :
        print(criti(s[i]))

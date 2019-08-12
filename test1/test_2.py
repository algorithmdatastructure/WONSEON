# from exceptions import ValueError, EOFError

N = -1
while N <= 0:
    try :
        N = int(input())
        if N < 1 or N > 10000000 :
            print('Don\'t be a fool ')
    except (ValueError, EOFError) :
            print('Invalid response')

n = input().split()

M = -1
while M <= 0:
    try :
        M = int(input())
        if M < 1 or M > 100000 :
            print('Don\'t be a fool ')
    except (ValueError, EOFError) :
            print('Invalid response')

m = input().split()

# dict로 풀기
# a = {}
# for i in m :
#     if i in n :
#         a[i] = 1
#     else :
#         a[i] = 0
#
# print(*a.values())



# list로 풀기
a = []
for i in range(M) :
    if m[i] in n :
        a.append(1)
    else :
        a.append(0)

print(" ".join((str(i) for i in a)))
# print(*a)W

import math

c = int(input())

mylist = []
for i in range(c) :
    t = [a for a in input().split()]
    mylist.append(t)

# com = ['O(N)', 'O(N^2)', 'O(N^3)', 'O(2^N)', 'O(N!)']

def cal(x) :
    x[1:] = list(map(int, x[1:]))

    if 'O(N)' == x[0] :
        if 1e8 * x[3] >= x[1] * x[2] :
            return "May Pass."
        else : return "TLE!"

    elif 'O(N^2)' == x[0] :
        if 1e8 * x[3] >= (x[1]**2) * x[2] :
            return "May Pass."
        else : return "TLE!"

    elif 'O(N^3)' == x[0] :
        if 1e8 * x[3] >= (x[1]**3) * x[2] :
            return "May Pass."
        else : return "TLE!"

    elif 'O(2^N)' == x[0] :
        if 1e8 * x[3] >= (2**x[1]) * x[2] :
            return "May Pass."
        else : return "TLE!"

    else :
        if 1e8 * x[3] >= (math.factorial( x[1]) ) * x[2] :
            return "May Pass."
        else : return "TLE!"


for i in range(c) :
    print(cal(mylist[i]))

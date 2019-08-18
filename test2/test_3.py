from math import log

# 풀이 1
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return log(n, 3).is_integer()
# 풀이 2
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 :
            return False

        while n % 3 == 0:
            n /= 3

        if n == 1 : return True
        else : return False




if __name__ == '__main__' :
#    sol = Solution()
#    print(sol.isPowerOfThree(34))

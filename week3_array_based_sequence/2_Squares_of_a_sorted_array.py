# T(N) = O(NlogN)
class Solution:
    def sortedSquares(self, A: list[int]) -> list[int]:
        squares = lambda x: x**2

        A=list(map(squares, A))
        A=sorted(A)
        # return sorted([i**2 for i in A])
        return A


a = [-4,1,5,2]
print(Solution.sortedSquares(a))

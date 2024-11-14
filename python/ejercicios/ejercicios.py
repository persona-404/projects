class Solution:
    def countOdds(self, low, high):
        if low % 2 == 0 and high % 2 == 0:
            return (high-low)//2
        else:
            return ((high-low)//2) + 1


solution = Solution()

print(solution.countOdds(14,17))
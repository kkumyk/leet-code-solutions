"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.
"""


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # the value float("inf") represents positive infinity
        # use float(‘inf’) as an integer to represent it as infinity
        # the use for float('inf') is to give an infinite upperbounds when doing comparisons of int values
        
        first = second = float('inf')
        
        for n in nums: 
            if n <= first: 
                first = n
            elif n <= second:
                second = n
            else: # whenever third > first AND > second, go to the else clause
                return True
        return False


solution = Solution()
print(solution.increasingTriplet([5,4,3,2,1])) # false
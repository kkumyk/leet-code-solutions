"""
charSet - a box where we keep track of the letters we have seen SO FAR without repeating

l and r:
    - left and right pointers will determine a sliding window 
    - point to different positions in the string
    - help to define a substring between them
    - l (left pointer) will be initialised with 0
    - r (right pointer) will be changing as we visit every character while it will be using in the for loop
    - r (right) will go over every single character
    
"""

class Solution:
    def lengthOfTheLongestSubstring(self, s: str) -> int:
        
        charSet = set() 
        l = 0
        res = 0
        
        for r in range(len(s)):
            #  if s[r] not in seen, we can keep increasing the window size by moving right pointer
            while s[r] in charSet: # if we come across a duplicate char with r, we will update our set
                charSet.remove(s[l]) # remove that duplicate until that duplicate remains in char set
                l += 1 
            charSet.add(s[r])
            res = max(res, r - 1 + 1)
        return res


solution = Solution()
print(solution.lengthOfTheLongestSubstring("abcabcbb"))  # 3
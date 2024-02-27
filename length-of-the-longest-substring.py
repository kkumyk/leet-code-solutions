class Solution:
    def lengthOfTheLongestSubstring(self, s: str) -> int:
        
        charSet = set() 
        # left and right pointers will determine a sliding window 
        l = 0 # our left will be initialised with 0
        res = 0

        # the right one will be changing as we visit every character while it will be using in the for loop
        
        for r in range(len(s)): # the right pointer will go over every single character
            while s[r] in charSet: # if we come across a duplicate char with the right pointer r, we will update our set
                charSet.remove(s[l]) # remove that duplicate until that duplicate remains in char set
                l += 1 
            charSet.add(s[r])
            res = max(res, r - 1 + 1)
        return res


solution = Solution()
print(solution.lengthOfTheLongestSubstring("abcabcbb"))  # 3

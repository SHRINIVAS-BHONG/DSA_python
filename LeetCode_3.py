# variable length Sliding Window- Leetcode 3

class solution:
    def LengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        sett = set()
        n = len(s)

        # O(n) time complexity
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            w = (r-l)+1
            longest = max(longest, w)
            sett.add(s[r])
        
        return longest

print(solution().LengthOfLongestSubstring("abcabcbb"))

# time : O(n)
# space : O(n)
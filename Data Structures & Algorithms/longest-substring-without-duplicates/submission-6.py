class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "" :
            return 0
        l, r=0,1
        ls = 1
        while r != len(s):
            print(s[l:r])
            if s[r] in s[l:r]:
                l+=1
            else:
                r+=1

            ls = max(ls, r-l)

        return ls
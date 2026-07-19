class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        
        if s == "" :
            return 0
        l, r=0,1
        freq[s[0]] = 1
        ls = 1
        while r != len(s):
            if freq.get(s[r], 0) == 0:
                freq[s[r]] = 1
                r+=1
            else:
                freq[s[l]] = 0
                l+=1

            print(freq)

            ls = max(ls, r-l)

        return ls
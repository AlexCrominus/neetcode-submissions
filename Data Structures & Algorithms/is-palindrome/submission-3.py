class Solution:
    def isPalindrome(self, s: str) -> bool:
       
    #    s = "".join( a for a in s.split(" ")).lower()
        s = "".join( a for a in s if a.isalnum()).lower() 
        print(s)
        return s == s[::-1]
       


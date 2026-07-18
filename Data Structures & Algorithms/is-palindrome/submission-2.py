class Solution:
    def isPalindrome(self, s: str) -> bool:
       
       s = "".join( a for a in s.strip().split(" ")).lower()
       s = "".join( a for a in s if a.isalnum()) 

       return s == s[::-1]
       


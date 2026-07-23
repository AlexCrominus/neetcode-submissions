class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""

        for n in strs:
            ret += str(len(n))+"."+n

        return ret

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        ret = []
        i=0
        length=""
        sw = True

        while i != len(s):
            if not sw:


                word = ""
                length = int(length)
                for _ in range(length):
                    word += s[i]
                    i+=1 

                ret.append(word)
                sw = True
                length = ""
            elif s[i] != "." and sw:
                length += s[i]
                i += 1
            else: 
                sw = False
                i+=1
        if s[i-1] == ".":
            ret.append("")
        
        return ret
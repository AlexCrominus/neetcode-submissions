class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) == 1:
            return [strs]

        # in order to distinguish anagrams we need 2 things
        # 1 length
        # frequency vector

        anMap = {}

        for i, word in enumerate(strs):
            
            wordMap = {}

            for letter in word:
                wordMap[letter] = 1 + wordMap.get(letter, 0)

            key = frozenset(wordMap.items())
            anMap.setdefault(key, []).append(word)

        return list(anMap.values())

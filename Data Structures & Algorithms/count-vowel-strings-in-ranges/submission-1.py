class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowel = ["a", "e", "i", "o", "u"]

        cnt = []
        for query in queries:
            result = 0
            for i in range(query[0],query[1]+1,1):
                if words[i][0] in vowel and words[i][-1] in vowel:
                    result += 1
            cnt.append(result)

        return cnt

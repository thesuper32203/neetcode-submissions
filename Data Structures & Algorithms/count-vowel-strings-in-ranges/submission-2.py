class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowel = ["a", "e", "i", "o", "u"]

        end = [word[0] in vowel and word[-1] in vowel for word in words]

        cnt = []
        for query in queries:
            cnt.append(sum(end[query[0]:query[1]+1]))
        
        return cnt
        

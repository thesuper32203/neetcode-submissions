class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        results = defaultdict(list)

        for word in strs:

            key = [0] * 26

            for c in word:

                key[ord(c) - ord("a")] += 1
            
            if results.get(tuple(key), []) is None:

                results[tuple(key)] = word
            else:
                results[tuple(key)].append(word)

        return list(results.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            letter = sorted(word)
            sig = "".join(letter)
            if sig not in groups:
                groups[sig] = [word]
            else:
                groups[sig].append(word)
        result = []
        for group in groups.values():
            result.append(group)
        return result
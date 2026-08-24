class Solution:

    def encode(self, strs: List[str]) -> str:
        en_str = ""
        for s in strs:
            len_s = len(s)
            piece = str(len_s) + "#" + s
            en_str = en_str + piece
        return en_str

    def decode(self, en_str: str) -> List[str]:
        result = []
        i = 0
        while i < len(en_str):
            j = i
            while en_str[j] != "#":
                j = j + 1
            len_str = en_str[i:j]
            length = int(len_str)
            start = j + 1
            end = start + length
            actual_str = en_str[start:end]
            result.append(actual_str)
            i = end
        return result


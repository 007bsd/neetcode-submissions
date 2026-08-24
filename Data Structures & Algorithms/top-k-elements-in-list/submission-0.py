class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] = count[num] + 1
        freq_list = []
        for num, freq in count.items():
            pair = (freq, num)
            freq_list.append(pair)
        freq_list.sort(reverse=True)
        result = []
        for i in range(k):
            freq, num = freq_list[i]
            result.append(num)
        return result
        
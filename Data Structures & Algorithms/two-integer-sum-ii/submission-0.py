class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        # [4, 5, 6, 7], target = 10
        # 1-indexed so return [1, 3]
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left = left + 1
            else:
                right = right - 1
        return []

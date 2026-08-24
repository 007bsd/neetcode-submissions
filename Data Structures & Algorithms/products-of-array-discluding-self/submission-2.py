class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # [2, 3, 4]
        # give all 1
        answer = [1] * n
        # start with index 1, 0 has already 1
        for i in range(1, n):
            # multiply index 1 with the previous one
            answer[i] = answer[i -1] * nums[i-1]
        # [1, 2, 6]
        # start now from the extreme right

        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * right
            right = right * nums[i]
        return answer

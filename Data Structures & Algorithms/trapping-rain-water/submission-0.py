class Solution:
    def trap(self, height: List[int]) -> int:
        # Input: height = [0,2,0,3,1,0,1,3,2,1]
        # output = 0
        if len(height) < 3:
            return 0

        n = len(height)

        left_max = [0] * n

        left_max[0] = height[0]

        for i in range(1, n):
            left_max[i] = max(left_max[i -1], height[i])

        right_max = [0] * n
        right_max[n - 1] = height[n - 1]

        for i in range(n -2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        total_water = 0
        for i in range(n):
            current_water_level = min(left_max[i], right_max[i])
            current_water = current_water_level - height[i]
            total_water = total_water + max(0, current_water)
        return total_water

        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Input: height = [1,7,2,5,4,7,3,6]
        # water_height = min( 7, 6)
        # width = 6
        # area = 36 
        max_area = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            left_height = heights[left]
            right_height = heights[right]
            water_height = min(left_height, right_height)
            current_area = width * water_height
            if current_area > max_area:
                max_area = current_area
            if left_height < right_height:
                left = left + 1
            else: right = right - 1
        return max_area

        
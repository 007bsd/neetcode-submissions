class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # lets sort the number
        # [-1, 0, 1, 2, -1, -4]
        # [[-1, -2, 2], [-1, 0, 1]]
        nums.sort()
        result = []
        
        for i in range (len(nums)):
            # skip the first element from the calculaton
            # if duplicate numbers then skip
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # lets not positive numbers
            if nums[i] > 0:
                break
            # lets find the two numbers
            left = i + 1
            right = len(nums) -1
            target = 0 - nums[i]
            while left < right:
                two_sum = nums[left] + nums[right]
                # if it matches, found the pair
                if two_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    # now move the pointer 
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right -1]:
                        right = right - 1
                    left = left + 1
                    right = right - 1
                elif two_sum < target:
                    left = left + 1
                else: right = right -1
        return result

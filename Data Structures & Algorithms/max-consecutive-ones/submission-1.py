class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        check_index = 0
        for i, num in enumerate(nums):
            if num == 1:
                check_index = 0
                while(i+check_index < len(nums) and nums[i + check_index] == 1):
                    check_index += 1               
                if check_index > max_length:
                    max_length = check_index
        return max_length
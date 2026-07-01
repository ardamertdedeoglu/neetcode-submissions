class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concat = []
        for i in range(2 * len(nums)):
            concat.append(nums[i % len(nums)])
        
        return concat
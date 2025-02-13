from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0]*(2*length)

        if length == 0:
            return nums
        for i in range(length):
            answer[i] = nums[i]
            answer[i+length] = nums[i]
        return answer
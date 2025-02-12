from typing import List
class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        dictionary = dict()
        for idx, value in enumerate(nums):
            to_find = target - value
            if to_find in dictionary:
                return [idx, dictionary[to_find]]
            dictionary[value] = idx
        return []
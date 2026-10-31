class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


#########################################################################################


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}

        for i in range(len(nums)):
            map[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in map and map[complement] != i:
                return[i, map[complement]]
        return []

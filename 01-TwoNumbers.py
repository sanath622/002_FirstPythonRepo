class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for num in range(len(nums)):
            
            pm = target - nums[num]
            if (pm in mem):
                return [mem[pm], num]
            else:
                mem[nums[num]] = num

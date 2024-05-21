from typing import List


    def moveZeroes(nums: List[int]) -> None:
            start = 0
            end = len(nums)-1
            while(start < end):
                if(nums[start] == 0):
                    zero = nums.pop(start)
                    nums.insert(end,zero)
                    end -= 1
                else:
                    start += 1
                 
            

nums = [0]
moveZeroes(nums)
print(nums)
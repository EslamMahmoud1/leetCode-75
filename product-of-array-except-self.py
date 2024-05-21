from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    product = 1
    realProduct = 1
    zeroCount = 0
    for num in nums:
        if(num == 0): zeroCount += 1
        product *= num if num != 0 else 1
        realProduct *= num
    for i in range(len(nums)):
        if(zeroCount <= 1):
            nums[i] = (int)(realProduct / nums[i]) if nums[i] != 0 else product
        elif(zeroCount > 1):
            nums[i] = 0
    return nums
    

nums = [1,2,3,4]
x = productExceptSelf(nums)
print(x)
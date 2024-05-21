from typing import List


def increasingTriplet(nums: List[int]) -> bool: 
    n = len(nums)
    min_arr = [0] * len(nums)
    max_arr = [0] * len(nums)

    min_arr[0] = nums[0]
    max_arr[-1] = nums[-1]

    for i in range(1,n):
        min_arr[i] = nums[i] if min_arr[i-1] > nums[i] else min_arr[i-1]
    
    for i in range(n - 2, -1, -1):
        max_arr[i] = nums[i] if max_arr[i+1] < nums[i] else max_arr[i+1]

    for i in range(1,n-1):
        if(min_arr[i] < nums[i] < max_arr[i]):
            return True
    return False

nums = [2,1,6,0,4,5]
x = increasingTriplet(nums)
print(x)
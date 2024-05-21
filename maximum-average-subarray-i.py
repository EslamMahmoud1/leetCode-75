from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    slidingSum = sum(nums[0 : k ]) 
    leftPointer = 1
    rightPointer = leftPointer + k - 1
    maxSum = slidingSum
    
    while(rightPointer < len(nums)):
        slidingSum = slidingSum + nums[rightPointer] - nums[leftPointer - 1]
        if(slidingSum > maxSum):
            maxSum = slidingSum
        leftPointer += 1
        rightPointer += 1
    return maxSum / k

nums = [1,12,-5,-6,50,3]
k = 4
x = findMaxAverage(nums,k)
print(x)
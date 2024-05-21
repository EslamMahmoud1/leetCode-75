from typing import List


def maxArea(height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    maxArea = 0
    while(l < r):
        area = (min(height[l] , height[r]) * (r - l))
        if(area > maxArea):
            maxArea = area
        if(height[l] < height[r]):
            l += 1
        elif(height[r] < height[l]):
            r -= 1
        else:
            if(l < r): l += 1
            else: r-= 1
    return maxArea

height = [1,8,6,2,5,4,8,3,7]
x= maxArea(height)
print(x)

        
            



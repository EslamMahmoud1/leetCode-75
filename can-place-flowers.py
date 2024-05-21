from typing import List
def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    plantCount = 0
    length = len(flowerbed)
    i = 0
    while i < length:
        left = i - 1
        right = i + 1
        if flowerbed[i] == 0 and (left < 0 or flowerbed[left] == 0) and (right >= length or flowerbed[right] == 0):
            plantCount += 1
            i += 1  
        i += 1 
    return plantCount >= n



flowerbed = [1,0,0,0,1,0,0]
n = 2
x = canPlaceFlowers(flowerbed , n)  
print(x)      


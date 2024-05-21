from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    out = []
    greatest = max(candies)
    for candy in candies:
        if(candy + extraCandies >= greatest):
            out.append(True)
        else:
            out.append(False)
    return out

        


candies = [2,3,5,1,3]
x = kidsWithCandies(candies,3)
print(x)
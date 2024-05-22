
def maxVowels(s: str, k: int) -> int:
    def isVowel(char) -> bool:
        if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):return True
        else : return False

    def initCalc(subStr):
        maxCount = 0
        for c in subStr:
            if(isVowel(c)):
                maxCount += 1
        return maxCount
    
    initSubStr = s[0:k]
    maxCount = initCalc(initSubStr)
    left = 1
    right = left + k -1
    count = maxCount
    while(right < len(s)):
        if(isVowel(s[left - 1])):
            count -= 1
        if(isVowel(s[right])):
            count += 1
        maxCount = max(maxCount , count)
        left += 1
        right += 1

    return maxCount

s = "abciiidef"
k = 3
x = maxVowels(s,k)
print(x)



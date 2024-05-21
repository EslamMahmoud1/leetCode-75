def is_vowel(char):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return char in vowels

    def reverseVowels(s: str) -> str:
        left, right = 0, len(s) - 1 
        strList = list(s)
        while(left < right):
            if(is_vowel(strList[left]) and is_vowel(strList[right])):
                strList[left] , strList[right] = strList[right] , strList[left]
                left += 1
                right -= 1 
            elif(is_vowel(strList[left])):
                right -= 1 
            elif(is_vowel(strList[right])):
                left += 1
            else:
                left += 1
        return ''.join(strList)

s = "hello"
x = reverseVowels(s)
print(x)
    

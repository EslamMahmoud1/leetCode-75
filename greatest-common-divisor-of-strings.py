def gcdOfStrings(str1: str, str2: str) -> str:
    mins = min(len(str1),len(str2))
    minStr =""
    maxStr =""
    if(len(str1) == mins ):
        minStr = str1
        maxStr = str2
    else :
        minStr = str2
        maxStr = str1

    i=mins
    while(i > 0 ):
        s = minStr[0:i]
        if((minStr.count(s) * len(s) == len(minStr) and (maxStr.count(s) * len(s) == len(maxStr)))):
            return s
        i-=1
    return ""


str1 = "LEET"
str2 = "ABAB"

res = gcdOfStrings(str1,str2)

print(res)



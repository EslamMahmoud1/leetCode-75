def isSubsequence(s: str, t: str) -> bool:
    sPointer = 0
    tPointer = 0

    for tPointer in range(len(t)):
        if(sPointer == len(s)):
            break
        
        if(t[tPointer] == s[sPointer]):
            sPointer += 1

    if(sPointer < len(s)):
        return False
    else:
        return True
    
s = "axc"
t = "ahbgdc"

x = isSubsequence(s,t)
print(x)
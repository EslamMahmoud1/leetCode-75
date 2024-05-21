def mergeAlternately(word1: str, word2: str) -> str:
    out = []
    count1 = len(word1)
    count2 = len(word2)
    p1 = 0
    p2 = 0
    i = 0

    while((p1 == i and p1<count1) | (p2 == i and p2 < count2)):
        if((p1 == i and p1<count1) and (p2 == i and p2 < count2)):
            out.append(word1[p1])
            out.append(word2[p2])
            p1 +=1
            p2 +=1
        elif((p1 == i and p1<count1)):
            out.append(word1[p1])
            p1 +=1
        elif((p2 == i and p2 < count2)):
            out.append(word2[p2])
            p2 +=1
        i +=1
    return ''.join(out)


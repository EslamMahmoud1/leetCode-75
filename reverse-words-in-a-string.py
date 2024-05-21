def reverseWords(s: str) -> str:
    cleanS = s.strip()
    orderdList = cleanS.split(" ")
    reversedList = [x for x in orderdList if x != '']
    reversedList.reverse()
    return " ".join(reversedList)


str = "a good   example"
x = reverseWords(str)
print(x)
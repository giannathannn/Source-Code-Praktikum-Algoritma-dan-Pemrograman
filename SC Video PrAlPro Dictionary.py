
def StrtoDict(String):
    String = String.lower()
    StringList = []
    KeyList = []
    ValueList = []
    Dict = dict()
    JumChar = 0

    for i in String:
        StringList.append(i)

    for l in range(3):
        for j in StringList:
            while j in StringList:
                if j in StringList:
                    JumChar += 1
                    StringList.remove(j)
            KeyList.append(j)
            ValueList.append(JumChar)
            JumChar = 0

    Len = len(KeyList)
    for k in range(Len):
        Dict[KeyList[k]] = ValueList[k]

    return Dict

Word = "Satoshi"
print(StrtoDict(Word))
Word1 = "Pemrograman"
print(StrtoDict(Word1))

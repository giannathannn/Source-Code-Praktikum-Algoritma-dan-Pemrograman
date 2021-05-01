
def TupleSort(List):
    # Str > Float
    NewList = list()
    TempoList = list()
    for a in List:
        for b in a:
            if 'item' in b:
                TempoList.append(b)
            else:
                b = float(b)
                TempoList.append(b)
        NewList.append(TempoList)
        TempoList = []

    # Sorting
    Len = len(NewList)
    for i in range(Len):
        for j in range(0,Len-i-1):
            if NewList[j] < NewList[j+1]:
                NewList[j], NewList[j+1] = NewList[j+1], NewList[j]

    # List > Tuple
    for y in range(2):
        for x in NewList:
            Tuple = tuple(x)
            NewList.append(Tuple)
            NewList.remove(x)

    return NewList

price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
#[('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
print(TupleSort(price))

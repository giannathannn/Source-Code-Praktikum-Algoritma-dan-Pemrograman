
HandleR1 = open('/media/thannntzy/Local Disk/Linux/Mata Kuliah/Semester 2/Praktikum Algoritma dan Pemrograman/Week 12/p1.txt','r')
HandleR2 = open('/media/thannntzy/Local Disk/Linux/Mata Kuliah/Semester 2/Praktikum Algoritma dan Pemrograman/Week 12/p2.txt','r')

List1 = list()
for line in HandleR1:
    P = line.split()
    for i in P:
        i = i.lower()
        List1.append(i)
    P = []
List2 = list()
for line in HandleR2:
    P = line.split()
    for i in P:
        i = i.lower()
        List2.append(i)
    P = []
List1 = set(List1)
List2 = set(List2)
ListAll = list()
ListAll.append(List1)
ListAll.append(List2)
ResultI = ListAll[0]
ResultD = ListAll[0]
ResultSD = ListAll[0]
for i in range(1,len(ListAll)):
    ResultI = ResultI.intersection(ListAll[i])
    ResultD = ResultD.difference(ListAll[i])
    ResultSD = ResultSD.symmetric_difference(ListAll[i])

print("Intersection: ")
print(ResultI)
print("Difference: ")
print(ResultD)
print("Symmetric Difference: ")
print(ResultSD)
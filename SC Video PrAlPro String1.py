'''
Codeforces 71 A
Way Too Long Word
'''

#Input
n = int(input())

#Program
output = []
for i in range(n):
    Word = str(input())
    if len(Word) >= 10:
        b = len(Word) - 2
        b = str(b)
        a = Word[0] + b + Word[-1]
        a = output.append(a)
    else:
        a = output.append(Word)
for j in output:
    print(j)
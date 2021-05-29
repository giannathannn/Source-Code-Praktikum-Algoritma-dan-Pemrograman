
vokal = 'aiueo'

def IteratifConsonant(Str):
    Sum = 0
    for i in range(len(Str)):
        if Str[i].lower() not in vokal and Str[i].isalpha():
            Sum += 1
    return Sum

def RecursiveConsonant(Str):
    if Str == '':
        return 0

    if Str[0].lower() not in vokal and Str[0].isalpha():
        return 1 + RecursiveConsonant(Str[1:])
    else:
        return RecursiveConsonant(Str[1:])

a = 'PrakAlPro'
print(RecursiveConsonant(a))

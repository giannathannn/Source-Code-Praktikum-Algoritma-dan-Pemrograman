
def prima(n):
    Result = [2]
    for i in range(3,n):
        Cek = 1
        for j in range(2,i-1):
            if i % j == 0:
                Cek = 0
        if Cek == 1:
            Result.append(i)
    for k in Result:
        print(k,end=", ")

print(prima(10))
print(prima(100))

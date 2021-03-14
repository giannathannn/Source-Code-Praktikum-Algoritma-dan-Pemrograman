'''
Codeforces 217 A
Perfect Pair
'''

'''
Let us call a pair of integer numbers m-perfect,
if at least one number in the pair is greater than or equal to m.
Thus, the pairs (3, 3) and (0, 2) are 2-perfect while the pair (-1, 1) is not.

Two integers x, y are written on the blackboard.
It is allowed to erase one of them and replace it with the sum of the numbers, (x + y).

What is the minimum number of such operations one has to perform in order to
make the given pair of integers m-perfect?
'''

#Input
x = int(input())
y = int(input())
m = int(input())

#Proses
output = 0
if x > 0 or y > 0:
    while x < m and y < m:
        if x < y:
            x += y
        else:
            y += x
        output += 1
else:
    output = -1
    
print(output)

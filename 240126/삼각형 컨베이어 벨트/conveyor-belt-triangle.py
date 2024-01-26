n, t = map(int,input().split())

tri1=list(map(int,input().split()))
tri2=list(map(int,input().split()))
tri3=list(map(int,input().split()))

def belt():
    temp1 = tri1[n-1]
    temp2 = tri2[n-1]

    for i in range(n-1,0,-1):
        tri1[i]=tri1[i-1]
    tri1[0]=tri3[n-1]
    
    for i in range(n-1,0,-1):
        tri2[i]=tri2[i-1]
    tri2[0]=temp1

    for i in range(n-1,0,-1):
        tri3[i]=tri3[i-1]
    tri3[0]=temp2

for i in range(t):
    belt()

for el in tri1:
    print(el, end=' ')
print('')
for el in tri2:
    print(el, end=' ')
print('')
for el in tri3:
    print(el, end=' ')
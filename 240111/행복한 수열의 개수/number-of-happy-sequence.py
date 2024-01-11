n,m=map(int,input().split())

if m==1:
    print(2*n)
    quit()

arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))

row_max=0
temp_row_max=0
col_max=0
temp_col_max=0

mCnt=0

for col in range(n-1):
    for row in range(n-1):
        if arr[row][col] == arr[row+1][col]:
            temp_row_max+=1
            row_max=temp_row_max
            continue
        else:
            temp_row_max=0
            continue
    if row_max>=m:
        mCnt+=1

for row in range(n-1):
    for col in range(n-1):
        if arr[row][col] == arr[row][col+1]:
            temp_col_max+=1
            col_max=temp_col_max
            continue
        else:
            temp_col_max=0
            continue
    if col_max>=m:
        mCnt+=1

print(mCnt)
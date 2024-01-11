N=int(input())

arr=[]
max_gold=0

def get_gold_num(row_s,col_s,row_e,col_e):
    goldCnt=0
    for row in range(row_s,row_e+1):
            for col in range(col_s,col_e+1):
                goldCnt+=arr[row][col]
    return goldCnt

for i in range(N):
    arr.append(list(map(int, input().split())))

for row in range(N):
        for col in range(N):
            if row+2>=N or col+2>=N:
                continue
            goldCnt=get_gold_num(row,col,row+2,col+2)
            max_gold=max(max_gold,goldCnt)

print(max_gold)
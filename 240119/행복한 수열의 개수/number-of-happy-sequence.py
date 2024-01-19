n,m=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(n)]

seq=[0 for _ in range(n)]

def is_happy_seq():
    #주어진 seq가 행복한 수열인지 판단하는 함수
    consecutive_count,max_ccnt= 1, 1
    for i in range(1,n):
        if seq[i-1]==seq[i]:
            consecutive_count+=1
        else:
            consecutive_count=1

        max_ccnt=max(max_ccnt,consecutive_count)

    return max_ccnt>=m

num_happy=0

for i in range(n):
    seq=arr[i][:]

    if is_happy_seq():
        num_happy+=1

for j in range(n):
    for i in range(n):
        seq[i]=arr[i][j]

    if is_happy_seq():
            num_happy+=1

print(num_happy)
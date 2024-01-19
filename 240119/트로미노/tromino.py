n, m = map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(n)]

def max_tromino():
    temp_max,max_L_shaped,max_I_shaped=0,0,0
    #ㄴ자 모양의 값의 합을 구함
    for j in range (m-1):
        for i in range(n-1):
            temp_max=arr[i][j]+arr[i][j+1]+arr[i+1][j+1]
            max_L_shaped=max(temp_max,max_L_shaped)
    #ㄴ의 좌우반전 모양의 값의 합을 구함
    for j in range (m-1):
        for i in range(1,n):
            temp_max=arr[i][j]+arr[i][j+1]+arr[i-1][j+1]
            max_L_shaped=max(temp_max,max_L_shaped)

    #ㄱ자 모양의 값의 합을 구함
    for j in range (m-1):
        for i in range(n-1):
            temp_max=arr[i][j]+arr[i+1][j]+arr[i+1][j+1]
            max_L_shaped=max(temp_max,max_L_shaped)
    #ㄱ의 좌우반전 모양의 값의 합을 구함
    for j in range (m-1):
        for i in range(1,n):
            temp_max=arr[i][j]+arr[i-1][j]+arr[i-1][j+1]
            max_L_shaped=max(temp_max,max_L_shaped)

    #ㅣ자 모양의 값의 합을 구함
    for j in range(m-2):
        for i in range(n):
            temp_max=arr[i][j]+arr[i][j+1]+arr[i][j+2]
            max_I_shaped=max(temp_max,max_I_shaped)

    #ㅡ자 모양의 값의 합을 구함
    for j in range(m):
        for i in range(n-2):
            temp_max=arr[i][j]+arr[i+1][j]+arr[i+2][j]
            max_I_shaped=max(temp_max,max_I_shaped)

    return max(max_L_shaped,max_I_shaped)

print(max_tromino())
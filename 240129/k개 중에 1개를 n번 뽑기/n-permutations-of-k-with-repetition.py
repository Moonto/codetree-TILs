k,n = map(int,input().split())

answer=[]

def print_answer():
    for el in answer:
        print(el,end=' ')
    print()

def choose(curr_n):
    if(curr_n==n+1):
        print_answer()
        return
    
    for i in range(1,k+1):
        answer.append(i)
        choose(curr_n+1)
        answer.pop()
    
    return

choose(1)
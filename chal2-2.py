from math import log
def answer(total_lambs):
    return (febo_index(total_lambs)-level(total_lambs))
def level(n):
    cnt=int(log(n,2))
    if (n-(2**cnt)+1)>=(2**(cnt-1)+2**(cnt-2)):
        cnt+=1
    return cnt

def febo_index(n):
    if n ==1:
        return 1
    elif n == 2:
        return 2
    total=2
    pre1=1
    pre2=1
    cnt=2
    while total<n:
        present =pre1+pre2
        total+=present
        pre2=pre1
        pre1=present
        cnt+=1
    if total>n:
        cnt-=1
    return cnt
print(answer(10))
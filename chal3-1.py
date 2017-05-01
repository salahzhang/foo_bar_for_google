def answer(n):
    F=[0]*201
    F[0]=1
    F[1]=1
    for i in range(2,201):
        k=200
        while k>i-1:
            F[k]=F[k]+F[k-i]
            k-=1
    return F[n]-1
print(answer(3))
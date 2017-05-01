from itertools import product
from fractions import Fraction

def sumRow(m, r):
    return sum(m[r])

def substract(matr_a, matr_b):
    output = []
    for i in range(len(matr_a)):
        tmp = []
        for valA, valB in zip(matr_a[i], matr_b[i]):
            tmp.append(valA - valB)
        output.append(tmp[:])
    return output[:]


def matrixmult(matr_a, matr_b):
    #cols = len(matr_b[0])
    rows = len(matr_b)
    if rows is not 0:
        cols = len(matr_b[0])
    else:
        cols = 0
    resRows = range(len(matr_a))
    rMatrix = [[0] * cols for _ in resRows]
    for idx in resRows:
        for j, k in product(range(cols), range(rows)):
            rMatrix[idx][j] += matr_a[idx][k] * matr_b[k][j]
    if cols is not 0:
        return rMatrix
    else:
        return 0


def invert(matrix):
    n = len(matrix)
    inverse = [[Fraction(0) for col in range(n)] for row in range(n)]
    for i in range(n):
        inverse[i][i] = Fraction(1)
    for i in range(n):
        for j in range(n):
            if i != j:
                if matrix[i][i] == 0:
                    return False
                ratio = matrix[j][i]/matrix[i][i]
                for k in range(n):
                    inverse[j][k] = inverse[j][k] - ratio * inverse[i][k]
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
    for i in range(n):
        a = matrix[i][i]
        if a == 0:
            return False
        for j in range(n):
            inverse[i][j] = inverse[i][j] / a
    return inverse

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a,n):
    ans = a[0]
    for i in range(1,n):
        ans = (a[i]*ans)//gcd(a[i],ans)
    return ans

def onematrix(n):
    res=[]
    for i in range(n):
        res.append([0]*n)
    for i in range(n):
        res[i][i]=1
    return res


def answer(m):
    num = len(m)
    if len(m[0])==1 and num==1:
        return [1,1]
    f = []
    # finding zero rows
    for i in range(0, num):
        j = []
        j.append(sumRow(m, i))
        j.append(i)
        f.append(j)
    cnt_r=[]
    cnt_i=[]
    for i in range(len(f)):
        if f[i][0]!=0:
            cnt_r.append(f[i][1])
        else:
            cnt_i.append(f[i][1])
    I=onematrix(len(cnt_r))
    R=[]
    for i in range(len(cnt_r)):
        R.append([0]*len(cnt_i))
    for i in range(len(cnt_r)):
        for j in range(len(cnt_i)):
            R[i][j]=Fraction(m[cnt_r[i]][cnt_i[j]],sumRow(m,cnt_r[i]))
    Q=[]
    for i in range(len(cnt_r)):
        Q.append([0]*len(cnt_r))
    for i in range(len(cnt_r)):
        for j in range(len(cnt_r)):
            Q[i][j]=Fraction(m[cnt_r[i]][cnt_r[j]],sumRow(m,cnt_r[i]))
    if len(Q)==len(m) or len(Q)==0:
        return [0,0]
    L=substract(I,Q)
    N=invert(L)
    res=matrixmult(N,R)
    if res == 0:
        return 0
    else:
        m =res[0]
    e=[]
    for i in range(0,len(m)):
        e.append(m[i].denominator)
    k=lcm(e,len(e))
    e=[]
    for i in range(0,len(m)):
        e.append((m[i].numerator*k)//m[i].denominator)
    e.append(k)
    return e


def length(posistion1,position2):
    return round(((posistion1[0]-position2[0])**2+ (posistion1[1]-position2[1])**2)**0.5,4)

def mirror(p1, p2,m,n,d):
    res=[]
    p=list(p2)
    while (p[0]-p1[0])<=d:
        res.append(list(p))
        p[0]+=m
    return res,p2
print mirror([1,1],[2,1],3,2,4)
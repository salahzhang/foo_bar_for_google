def answer(l):
    l.sort(reverse=True)
    deque0=[]
    deque1=[]
    deque2=[]
    for num in l:
        if num%3==0:
            deque0.append(num)
        elif num%3==1:
            deque1.append(num)
        else:
            deque2.append(num)
    res=[]
    if sum(l)%3==1:
        if deque1:
            deque1.pop()
        else:
            if deque2:
                deque2.pop()
            else:
                return 0
            if deque2:
                deque2.pop()
            else:
                return 0
    elif sum(l)%3==2:
        if deque2:
            deque2.pop()
        else:
            if deque1:
                deque2.pop()
            else:
                return 0
            if deque1:
                deque1.pop()
            else:
                return 0
    res=[]
    for num in deque0:
        res.append(num)
    for num in deque1:
        res.append(num)
    for num in deque2:
        res.append(num)
    res.sort()
    ans=0
    for i in range(len(res)):
        ans+=res[i]*(10**i)
    return ans

print(answer([9,3,4,1,1,5]))
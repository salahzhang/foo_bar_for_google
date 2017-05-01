# remove duplicate, not sort, reverse 
# nums=[4,2,3,1,2,4,1]
# size=len(nums)
# ans=[]
# for i in range(size):
# 	if nums[i] not in ans:
# 		ans.append(nums[i])
# # print ans

def qsort(L):
   if L == []: return []
   return qsort([x for x in L[1:] if x< L[0]]) + L[0:1] + \
          qsort([x for x in L[1:] if x>=L[0]])

print qsort([2,1,4,3])

# res=[]
# for i in range(len(ans)):
# 	a=max(ans)
# 	res.append(a)
# 	ans.remove(a)
# print res





# count how many 1 in num when transport to bianry
# num=8
# cnt=0
# if num < 0 : num=abs(num)
# while num != 0 :
# 	if num %2 == 1:
# 		cnt+=1
# 	num/=2
# print cnt




# 2 sum
# nums=[1,2,4,3,5]
# target = 7
# d={}
# for i in range(len(nums)):
# 	x = nums[i]
# 	if target-x in d:
# 		print [i,d[target-x]]
# 	else:
# 		d[x]=i
# print None



# nums=[1,2,3,4,1,2,4,1,3]
# i=1
# res=0
# while i < len(nums):
# 	res+=nums[i]
# 	i+=2
# print res






# import operator
# nums=[1,2,1,3,1,1,1,2,3,4,2,4,5,2,3]
# d={}
# for i in range(len(nums)):
# 	if nums[i] in d:
# 		d[nums[i]]+=1
# 	else:
# 		d[nums[i]]=1
# #sorted(d.values(),reverse=True)
# one = max(d.iteritems(), key=operator.itemgetter(1))[0]
# del d[one]
# print max(d.iteritems(), key=operator.itemgetter(1))[0]

# vector = [0]*len(nums)
# for num in nums:
# 	vector[num]+=1
# print vector
# one=max(vector)
# one_index=vector.index(one)
# vector[one_index]=0
# second=max(vector)
# print vector.index(second)


# nums=[1,2,1,3,1,1,1,2,3,4,2,4,5,2,3]
# ans=set(nums)
# ans.remove(max(ans))
# print max(ans)




# closet
# nums=[1,2,4,3,6,8]
# target=13
# nums.sort()
# res=nums[0]+nums[1]
# i,j=0,len(nums)-1
# while i<j:
# 	summ=nums[i]+nums[j]
# 	if summ==target:
# 	    print summ
# 	if abs(summ-target)<abs(res-target):
# 		res=summ
# 	if summ > target:
# 		j-=1
# 	if summ < target:
# 		i+=1
# print res
# for index add counter


# A=[1,0];B=[3,2];C=[0,2];D=[3,1];n=4
# if A[0]>B[0]: A,B=B,A
# if C[0]>D[0]: C,D=D,C
# def isNoSpace(A,B,C,D):
# 	if A[0]==D[0] and A[1]==C[1] and D[1]==B[1] and B[1]==C[1]:
# 		return True
# 	else:
# 		return False
# def allOnBodge(A,B,C,D,n):
# 	Node=[A,B,C,D]
# 	for i in range(1,n-2):
# 		for j in range(1,n-2):
# 			if [i,j] in Node:
# 				return False
# 	return True
# def findfunction(n1,n2):
# 	res=[]
# 	if n1[0]!=n2[0]:
# 		res.append(float((n1[1]-n2[1])/(n1[0]-n2[0])))
# 		res.append(n1[1]-res[0]*n1[0])
# 	return res
# if A==C and A==D and B==C and B==D:
# 	print True
# if isNoSpace(A,B,C,D):
# 	print True
# else:
# 	if allOnBodge(A,B,C,D,4):
# 		if A[0]==B[0] and c[0]==D[0]:
# 			if A[0]==C[0]:
# 				if (A[1]-C[1])*(B[1]-C[1])<0:
# 					print True
# 				elif (A[1]-C[1])*(A[1]-D[1])<0:
# 					print True
# 				else:
# 					print False
# 			else:
# 				print False
# 		elif A[0]==B[0] and C[0]!=D[0]:
# 			C_D=findfunction(C,D)
# 			intersectNode=C_D[0]*A[0]+C_D[1]
# 			if (intersectNode-A[1])*(intersectNode-B[1])<0:
# 				print True
# 			else:
# 				print False
# 		elif A[0]!=B[0] and C[0]==D[0]:
# 			A_B=findfunction(A,B)
# 			intersectNode=A_B[0]*C[0]+A_B[1]
# 			if (intersectNode-C[1])*(intersectNode-D[1])<0:
# 				print True
# 			else:
# 				print False
# 		else:
# 			A_B=findfunction(A,B)
# 			C_D=findfunction(C,D)
# 			print A_B,C_D
# 			if A_B[0]==C_D[0]:
# 				if A_B[0]==0:
# 					if A[1]==B[1] and B[1]==C[1] and C[1]==D[1]:
# 						if (C[0]-A[0])*(C[0]-B[0])<0:
# 							print True
# 						if (A[0]-C[0])*(A[0]-D[0])<0:
# 							print True
# 					else:
# 						print False
# 				else:
# 					print False
# 			else:
# 				intersectIndex=[]
# 				intersectIndex.append((C_D[1]-A_B[1])/(A_B[0]-C_D[0]))
# 				intersectIndex.append(intersectIndex[0]*A_B[0]+A_B[1])
# 				print intersectIndex
# 				if (intersectIndex[0]-C[0])*(intersectIndex[0]-D[0])<=0 and (intersectIndex[0]-A[0])*(intersectIndex[0]-B[0])<=0:
# 					print True
# 				else:
# 					print False




# nums=[1,2,3,4,5]
# k=1
# if k>0:
#     print len(set(nums)&{n+k for n in nums})
# elif k==0:
#     cnt=0
#     for v in collections.Counter(nums).values():
#         if v>1:
#             cnt+=1
#     print cnt
# else:
#     print 0


# def count(n):
# 	res=set()
# 	for i in range(1,10000):
# 		for j in str(n*i).strip():
# 			res.add(j)
# 		if len(res)==10:
# 			return i*n
# 	return "never"
# t=int(input())
# for i in range(1,t+1):
# 	num=int(input())
# 	print('Case #',i,':',count(num))





# def revenge(s):
# 	cnt=0
# 	for i in range(1,len(s)):
# 		if s[i]!=s[i-1]:
# 			cnt+=1
# 	return cnt
# t=int(input())	
# for i in range(1,t+1):
# 	num=input().strip()+'+'
# 	print('Case #%d: %s' % (i+1, revenge(num)))




# def standing():
# 	n,s=input().strip().split()
# 	n=int(n)
# 	cnt=0
# 	stand=int(s[0])
# 	for i in range(1,n+1):
# 		if i > stand:
# 			cnt+=i-stand
# 			stand+=i-stand
# 		stand+=int(s[i])
# 	return cnt	
# t=int(input())	
# for i in range(1,t+1):
# 	print('Case #%d: %s' % (i, standing()))






# def standing():
#     s, k = input().strip().split()
#     k = int(k)
#     b = s.strip().split('+')
#     for i in range(len(b)):
#         if b[i] != '':
#             b[i] = -len(b[i])
#         else:
#             b[i] = 1
#     i=1
#     while i<len(b):
#         if b[i - 1] > 0 and b[i] > 0:
#             b[i - 1] += b[i]
#             b.remove(b[i])
#         else:
#             i+=1
#     for i in range(len(b)):
#         if b[i]>0:
#             b[i]+=1
#     cnt = 0
#     if b[0] == -k:
#         cnt += 1
#         b[0]*=-1
#     if b[-1] == -k:
#         cnt += 1
#         b[-1]*=-1
#     for i in range(1, len(b) - 1):
#         if b[i] > 0 and b[i - 1] == b[i + 1] and b[i] - b[i - 1] == k:
#             cnt += 2
#             b[i - 1] = b[i + 1] = -b[i - 1]
#     for i in range(1,len(b)):
#         if b[i - 1] == b[i] and b[i - 1] == 1 - k:
#             cnt += 2
#             b[i - 1] = b[i] = -b[i]
#     if min(b) < 0:
#         return "IMPOSSIBLE"
#     else:
#         return cnt
# t = int(input())
# for i in range(1, t + 1):
#     print('Case #%d: %s' % (i, standing()))

# def binarysearch(n):
#     l,r=0,len(n)-1
#     while l<r:
#         mid=(l+r)//2
#         if n[mid]<=n[mid+1]:
#             l=mid+1
#         else:
#             r=mid
#     return l


# def tidy():
#     n=input().strip()
#     if len(n)==1:
#         return n
#     i=0
#     peak=0
#     while i<len(n)-1:
#         if n[i]>n[i+1]:
#             break
#         elif n[i]==n[i+1]:
#             i+=1
#         else:
#             peak=i+1
#             i+=1
#     change=[0]*(len(n)-peak)
#     change[0]=int(n[peak])-1
#     for i in range(1,len(change)):
#         change[i]=9
#     last=''.join(str(change[i]) for i in range(len(change)))
#     res=[]
#     res.append(n[:peak])
#     res.append(last)
#     return int(''.join(res))
# t = int(input())
# for i in range(1, t + 1):
#     print('Case #%d: %s' % (i, tidy()))
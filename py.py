N=int(input())
arr=[]
for i in range(0,N):
    ar=int(input())
    arr.append(ar)
arr.sort()
n=int(N/2)
a1=arr[n]
a2=arr[n-1]
avg=a1+a2
print(avg)
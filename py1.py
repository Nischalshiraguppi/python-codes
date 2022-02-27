
a=input()
arr=[]
for i in a:
    arr.append(int(i))
leng=len(arr)
d=leng-1
e=0

for i in range(int(leng/2)):
    c=0
    a=0
    b=0
    a=arr[d]
    b=arr[e]
    c=a+b
    d=d-1
    e=e+1
    print(c,end="")

def ispalindrome(s):
    a=s[::-1]
    if a==s:
        return True
    return False
n=int(input())
leng=[]

for i in range(0,n):
    s=input()
    if ispalindrome(s):
        leng.append(len(s))
for i in range(0,n):
    print(leng[i])


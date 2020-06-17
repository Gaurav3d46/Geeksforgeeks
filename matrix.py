for i in range(int(input())):
    n=int(input())
    m=[]
    arr=list(map(int,input().split()))

    for j in range(0,len(arr),n):
        c=[]
        for k in range(j,j+n):
            c.append(arr[k])
        m.append(c)
    #transpose
    for j in range(n):
        for k in range(j,n):
            m[j][k],m[k][j]=m[k][j],m[j][k]
    t=[]
    for j in range(n):
        s=m[j]
        s.reverse()
        for k in range(len(s)):
            t.append(s[k])
    print(*t)

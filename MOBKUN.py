# cook your dish here
for t in range(int(input())):
    n,m,k,x=map(int,input().split())
    if(x % ((n*k)+m) == 0):
        print("Yes")
    elif((x % ((n*k)+m)) - (n*(k-1)) > 0):
        print("Yes")
    else:
        print("No")
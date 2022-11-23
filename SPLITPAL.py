# cook your dish here
for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    c=0
    i,j,ans=0,n-1,0
    while i<=j:
        if(arr[i]==arr[j]):
            i+=1 
            j-=1 
        elif (arr[i]<arr[j]):
            arr[j]-=arr[i]
            i+=1 
            ans+=1 
        else:
            arr[i]-=arr[j]
            j-=1 
            ans+=1
    print(ans)





    
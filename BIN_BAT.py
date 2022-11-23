# cook your dish here
import math
for t in range(int(input())):
    n,a,b=map(int,input().split())
    count=0
    x=math.log(n,2)
    #print(x)
    print((int(x) * a) + (int(x-1) * b))

# cook your dish here
for t in range(int(input())):
    string=input()
    n=len(string)
    if(string[0]==string[n-1]):
        print(n-2)
    else:
        print(2)
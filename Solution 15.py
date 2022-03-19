#WAS to print the following pattern
#1
#2 3
#4 5 6
n=int(input("Enter num of rows:"))
i=0
j=0
nu=1
for i in range(0,n):
    for j in range(0,i+1):
        print(nu,end="")
        nu=nu+1
    print("\r")

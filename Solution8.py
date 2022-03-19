#Was to print the  1 to n number using while loop.
n=int(input("Enter any number:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print("The sum of {} to {} is:{}".format(1,n,sum))

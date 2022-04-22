#WAS to enter 3 number and check whick number is maximum.
a=int(input("Enter num 1:"))
b=int(input("Enter num 2:"))
c=int(input("Enter num 3:"))
if(a>b and a>c):
    print("{} is Maximum Number:".format(a))
elif(b>a and b>c):
    print("{} is Maximum Number:".format(b))
elif(c>a and c>b):
    print("{} is Maximum Number:".format(c))
else :
    print("All numbers are Equal.")

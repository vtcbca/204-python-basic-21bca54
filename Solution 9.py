#WAP to Sum of digit.
no=int(input("Enter any num:"))
m=no
sum=0
re=0
while no!=0:
     re=no%10 
     sum=sum+re
     no=no//10
print("The sum of {} is {}.".format(m,sum))

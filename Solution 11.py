# WAP to enter any number and check itis armstrong or not.
no=int(input("Enter any num:"))
o=no
e=0
re=0
su=0
while no!=0:
      re=no%10
      e=re**3
      su+=e
      no=no//10
if(o==su):
    print("The {} is  Armstrong.".format(o))
else :
    print("The {} is not Armstrong.".format(o))

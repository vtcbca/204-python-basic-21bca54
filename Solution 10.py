# WAP to enter any number and cheacak itis palindrome or not
no=int(input("Enter any num:"))
o=no
e=0
re=0
su=0
while no!=0:
      re=no%10
      e=e*10+re
      
      no=no//10
if(o==e):
    print("The {} is  Palindrome.".format(o))
else :
    print("The {} is not Palindrome.".format(o))

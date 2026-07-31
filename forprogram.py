#Write a PYTHON program to print the natural numbers up to n
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(i)


#Write a PYTHON program to print even numbers up to n
n=int(input("enter the number:"))
print("even numbers",n)
for i in range(2,n+1,2):
    print(i)


#Write a PYTHON program to print odd numbers up to n
n=int(input("enter the number:"))
print("odd numbers",n)
for i in range(1,n-1,2):
    print(i)

#Write a PYTHON program that prints  1 2 4 8 16 32 … n2
n=int(input("enter the number:"))
i=1
while i<=n*n:
    print(i,end=" ")
    i=i*2


#Write a PYTHON program to sum the given sequence
#1 + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n!
n=int(input("enter the number:"))
sum=1
fact=1
for i in range(1,n+1):
    fact=fact*i
    sum=sum+(1/fact)
print("sum=",sum)


#Write a PYTHON program to compute the cosine series
# #cos(x) = 1 – x2 / 2! + x4 / 4! – x6 / 6! + … xn / n!
x=float(input("enter the x (in radians):"))
n=int(input("enter the highest even power (n):"))
sum=1
fact=1
sign=-1
for i in range(2,n+1,2):
    fact=1
    for j in range(1,i+1):
        fact*=j
    sum=sum+sign*(x**i)/fact
    sign*=-1
print("cos(",x,")=",sum)


#Write a short PYTHON program to check weather the
# #square root of number is prime or  not.
import math
n=int(input("enter a number:"))
root=int(math.sqrt(n))
if root*root!=n:
    print("not an integer.")
else:
    prime=True
    if root<2:
        prime=False
    else:
        for i in range(2,int(math.sqrt(root))+1):
            if root%i==0:
                prime=False
                break
    if prime:
        print("Square root is a Prime",root)
    else:
        print("Square root is Not a Prime",root)


     #Write a PYTHON program to produce following design
			#A B C
			#A B C
			#A B C
for i in range(3):
    for j in range(65,68):
        print(chr(j),end=" ")
    print()


#Write a PYTHON program to produce following design
     # A
      #A B
      #A B C
      #A B C D
      #A B C D E
      #If user enters n value as 5
n=int(input("enter n:"))
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()


#Write a PYTHON program to produce following design
       #A B C D E
       #A B C D
       #A B C
       #A B
       #A
      #(If user enters n value as 5)
n=int(input("enter n:"))
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()


#Write a PYTHON program to produce following
     # design
      #1
      #1 2
      #1 2 3
      #1 2 3 4
      #1 2 3 4 5
      #If user enters n value as 5
n=int(input("enter n: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


#Write a PYTHON program to produce following design
      #1
      #2 2
      #3 3 3
      #4 4 4 4
      #5 5 5 5 5
      #If user enters n value as 5
n=int(input("enter n:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()















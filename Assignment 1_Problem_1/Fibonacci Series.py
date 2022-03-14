#WAP to print fibonacci series
a=0
b=1
count = 0
n=int(input("Enter the numbers of elements:"))
if n ==0 or n == 11:
    print("""Please enter a valid input!!
Series must exist between 0 to 50""")
elif n == 1:
    print("The fibonacci series is:",a)
else:
    print("The fibonacci series is:")
    while count < n:
        print(a,end=" ")
        c=a+b
        a=b
        b=c
        count+=1
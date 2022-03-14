# WAP to count number of even and odd numbers from a series of numbers(user input available)
l=[]
n=int(input("Enter the number of elements in the list:"))
even = 0
odd = 0
for i in range(0,n):
    l.append(int(input()))
    if l[i] %2 == 0:
        even += 1
    else:
        odd += 1
print("Numbers of Even numbers:",even)
print("Numbers of Odd Numbers:",odd)                    
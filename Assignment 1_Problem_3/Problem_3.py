# WAP to count number of even and odd numbers from a series of numbers
t=(1,2,3,4,5,6,7,8,9) # also a list can be used
even = 0
odd = 0
for i in t:
    if i%2 == 0:
        even += 1
    else:
        odd += 1
print("Numbers of Even numbers:",even)
print("Numbers of Odd Numbers:",odd)
       

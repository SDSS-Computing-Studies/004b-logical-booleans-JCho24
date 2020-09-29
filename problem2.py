#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
a = input("Enter an integer: ")
a = float(a)

b = input("Enter an integer: ")
b = float(b) 

if a > b:
    a1 = a/b
    a2 = int(a1)

    if (a1 - a2) == 0:
        print(b ,end="")
        print(" is a factor of" ,end=" ")
        print(a)
    else:
        print(b ,end="")
        print(" is not a factor of" ,end=" ")
        print(a)

else:
    a1 = b/a
    a2 = int(a1)

    if (a1 - a2) == 0:
        print(a ,end="")
        print(" is a factor of" ,end=" ")
        print(b)
    else:
        print(a ,end="")
        print(" is not a factor of" ,end=" ")
        print(b)
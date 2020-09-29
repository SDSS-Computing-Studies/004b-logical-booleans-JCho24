"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is frue.
"""

#! python3

a = input("Enter a number: ")
a = float(a)

a1 = a/6
a2 = int(a1)


b1 = a/8
b2 = int(b1)


if (a1 - a2) == 0 and (b1 - b2) != 0:
    print(a ,end="")
    print(" is frue")
else:
    print(a ,end="")
    print(" is not frue")





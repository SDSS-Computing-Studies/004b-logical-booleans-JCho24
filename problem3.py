#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
a = input("Enter an integer: ")
a = float(a)

b = input("Enter an integer: ")
b = float(b) 

c = input("Enter an integer: ")
c = float(c) 

if c > b > a:
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

    if ((a**2) + (b**2) == (c**2)):
    print(a + ", " + b + ", " + c ,end=" ")
    print("form a Pythagorean triple")
    else:
    print(a + ", " + b + ", " + c ,end=" ")
    print("do not form a Pythagorean triple")
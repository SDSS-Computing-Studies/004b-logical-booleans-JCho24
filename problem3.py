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
a = input("Enter an integer: ").strip()
a = int(a)
a1 = str(a)

b = input("Enter an integer: ").strip()
b = int(b)
b1 = str(b)

c = input("Enter an integer: ").strip()
c = int(c)
c1 = str(c)

if a>b>c:
    if (a**2)==(b**2)+(c**2):
        print(c1+","+b1+","+a1+" form a Pythagorean triple")

    elif (a**2)!=(b**2)+(c**2):
        print(c1+","+b1+","+a1+" do not form a Pythagorean triple")
        
elif a>c>b:
    if (a**2)==(b**2)+(c**2):
         print(b1+","+c1+","+a1+" form a Pythagorean triple")

    elif (a**2)!=(b**2)+(c**2):
        print(b1+","+c1+","+a1+" do not form a Pythagorean triple")

elif b>a>c:
    if (b**2)==(a**2)+(c**2):
        print(c1+","+a1+","+b1+" form a Pythagorean triple")

    elif (b**2)!=(a**2)+(c**2):
        print(c1+","+a1+","+b1+" do not form a Pythagorean triple")

elif b>c>a:
    if (b**2)==(a**2)+(c**2):
        print(a1+","+c1+","+b1+" form a Pythagorean triple")

    elif (b**2)!=(a**2)+(c**2):
        print(a1+","+c1+","+b1+" do not form a Pythagorean triple")
        
elif c>a>b:
    if (c**2)==(b**2)+(a**2):
        print(b1+","+a1+","+c1+" form a Pythagorean triple")

    elif (c**2)!=(b**2)+(a**2):
        print(b1+","+a1+","+c1+" do not form a Pythagorean triple")

elif c>b>a:
    if (c**2)==(b**2)+(a**2):
        print(c1+","+b1+","+a1+" form a Pythagorean triple")

    elif (c**2)!=(b**2)+(a**2):
        print(c1+","+b1+","+a1+" do not form a Pythagorean triple")

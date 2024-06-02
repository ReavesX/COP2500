# Donald Jackson - quad.py - finds the roots and determinant for a given quadratic

# Writing functions to use later on
def determinant(a,b,c):
    determinantVal = b**2 - 4*(a * c)
    return determinantVal
def firstRt(a,b,c):
    x = (-b + (determinant(a,b,c))**(1/2))/(2*a)
    return x
def secondRt(a,b,c):
    x = (-b - (determinant(a,b,c))**(1/2))/(2*a)
    return x   

# Asking the user for inputs of a,b,c from a quadratic equation
a = float(input("Enter your function's a coefficient here:"))
b = float(input("Enter your function's b coefficient here:"))
c = float(input("Enter your function's c coefficient here:"))

# determining what to print based on the determinant's value 
if determinant(a,b,c) > 1:
    print(determinant(a,b,c))
    print("The function has two roots. One at",firstRt(a,b,c,), "and another at",secondRt(a,b,c,),".")  
elif determinant(a,b,c) == 0:
    print("The function has one root at:",firstRt(a,b,c))
else:
    print("Sorry, that quadratic has complex roots")
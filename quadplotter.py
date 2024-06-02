def quadraticFunction(a,b,c,x):
    y = a*x**2 + b*x + c 
    return y 

def printVal(a,b,c,x):
    print("The ordered pair is:(",x,",",round(quadraticFunction(a,b,c,x)),")",sep='')


# Donald Jackson - lineplotter.py - Returns values for the plot of a line

# Main Code Starts w/ initializing variables and creating an array to store x data points

a = float(input("Enter your function's a:"))
b = float(input("Enter your function's b:"))
c = float(input("Enter your function's c:"))
print("y =", a,"x^2 +", b,"x +",c)
x = [0,1,2,3,4,5,6,7,8,9]
i = 10
n = 1
for f in range(10): 
    printVal(a,b,c,x[f])
while i <= 100000:
    printVal(a,b,c,i**n)
    n=n+1
    if n == 8:
        break

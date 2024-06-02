# Donald Jackson - lineplotter.py - Returns values for the plot of a line

# Defining a function for slope intercept, and making a composite function to print the return value in a certain format. 
def slopeInt(m,b,x):
    y = m*x+b   
    return y
def printSlope(m,b,x):
    print("(",x,",",round(slopeInt(m,b,x),5),")",sep='') 


# Main Code Starts w/ initializing variables and creating an array to store x data points
x = [0,1,2,3,4,5,6,7,8,9,10,100,1000,10000,100000]
m = float(input("Enter your Slope here: "))
b = float(input("Enter your y-intercept here: "))
print("The equation of your line is: ", "y=",m,"x"," + ", b, sep='')
# For loop to return y values in the range x
for f in range(15): 
    printSlope(m,b,x[f])
#Donald Jackson - lakearea.py - This program takes the area of a half-circular
#lake.



#initializing variables
pi = 3.1416
lakeRadius = int(input("Enter the radius of the lake in meters."))



#Required arithmetic for area
areaOfLake = (pi * ((lakeRadius)**2))/2



#Returning area value for the given half-circle lake with r=lakeRadius
#The value is Rounded to 4 decimal places
print (str("The area of the lake is: ") + str((round(areaOfLake,4))) + str(" m^2"))

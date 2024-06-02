#Donald Jackson - courselist.py - allows the user to enter a list of courses, but stops them from addming more than 5 courses to the list.


# Fucntion to filter out "EXIT" 
def finalResult(class1,class2,class3,class4,class5):
    classes = [tooManyClasses(class1,class2,class3,class4,class5,class6)]
    if class2 == "EXIT" :
        print("Your Classes are:")
        print("1)",class1)
        classes = [class1]
    elif class3 == "EXIT":
        print("Your Classes are:")
        print("1)",class1)
        print("2)",class2)
        classes = [class1,class2]
    elif class4 == "EXIT" :
        print("Your Classes are:")
        print("1)",class1)
        print("2)",class2)
        print("3)",class3)
        classes = [class1,class2,class3]
    elif class5 == "EXIT":
        print("Your Classes are: ")
        print("1)",class1)
        print("2)",class2)
        print("3)",class3)
        print("4)",class4)
        classes = [class1,class2,class3,class4]
    elif class6 == "EXIT":
        print("Your Classes are: ")
        print("1)",class1)
        print("2)",class2)
        print("3)",class3)
        print("4)",class4)
        print("5)",class5)
        classes = [class1,class2,class3,class4,class5]
    return classes
#converting one-based to zero-based
def removeItPlease(removedVal):
    if removedVal == 1:
        removedVal = 0
    elif removedVal == 2:
        removedVal = 1
    elif removedVal == 3:
        removedVal = 2
    elif removedVal == 4:
        removedVal = 3
    elif removedVal == 5:
        removedVal = 4
    elif removedVal == 6:
        removedVal = 5
    return removedVal
def tooManyClasses(class1,class2,class3,class4,class5,class6):
    classes = [class1,class2,class3,class4,class5,class6]
    classes.pop(removeItPlease(int(input("Enter a number 1-6 to remove a class: "))))
    return classes
# Main Starts Here

classes = []
print("Type EXIT if you do not have a class for that slot")
class1 = input("Enter a class here: ")
class2 = input("Enter a class here: ")
class3 = input("Enter a class here: ")
class4 = input("Enter a class here: ")
class5 = input("Enter a class here: ")
class6 = input("Enter a class here: ")
print(finalResult(class1,class2,class3,class4,class5))
class7 = input("Input EXIT if you wish to receive your results, or you may add another class")
print(finalResult(class1,class2,class3,class4,class5))
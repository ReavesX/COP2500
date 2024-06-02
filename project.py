# Donald Jackson - project.py - 
# Purpose: Uses the grade cutoffs for the various classes I have this semester, and checks what the grade would be on the scale. While I understand that 
# this is redundant as canvas SHOULD already do this, some of the classes don't have it setup underneath the grades section of canvas/webcourses. This problem is solved by taking
# user input to determine for how many classes the type of grade range is, grade range type, and the input of the user's grade without a % sign  

#Function asks user for the type of grade range, then returns it as a dictionary given the inputs of the user, and also returns the type of grade range that was given for use
#in the other function. 
def gradeRange():
    gradeRangeType = input("Input the type of grading scale your class uses (Plus, Plus-Minus,None)").casefold().strip()
    if gradeRangeType == "plus-minus" or gradeRangeType == "plusminus" or gradeRangeType == "plus minus" or gradeRangeType == "plus/minus":
        # Taking the range literal of the  user inputs so it can form lists with the grades that are in the range.
        aPlus = [*range(int(input("input where your A+ range starts")),int(input("Input where your A+ range ends"))+1,1)]
        a = [*range(int(input("input where your A range starts")),int(input("Input where your A range ends"))+1,1)]
        aMinus = [*range(int(input("input where your A- range starts"))),int(input("Input where your A- range ends")+1,1)]
        bPlus = [*range(int(input("input where your B+ range starts")),int(input("Input where your B+ range ends"))+1,1)]
        b = [*range(int(input("input where your B range starts")),int(input("Input where your B range ends"))+1,1)]
        bMinus = [*range(int(input("input where your B- range starts")),int(input("Input where your B- range ends"))+1,1)]
        cPlus = [*range(int(input("input where your C+ range starts")),int(input("Input where your C+ range ends"))+1,1)]
        c = [*range(int(input("input where your C range starts")),int(input("Input where your C range ends"))+1,1)]
        cMinus = [*range(int(input("input where your C- range starts")),int(input("Input where your C- range ends"))+1,1)]
        fail = [*range(0,int(input("Input where your failure range ends"))+1,1)]
        gradeDict = [fail,cMinus,c,cPlus,bMinus,b,bPlus,aMinus,a,aPlus]
        return gradeDict,gradeRangeType
    elif gradeRangeType == "plus":
        # Taking the range literal of the  user inputs so it can form lists with the grades that are in the range.
        aPlus = [*range(int(input("input where your A+ range starts")),int(input("Input where your A+ range ends"))+1,1)]
        a = [*range(int(input("input where your A range starts")),int(input("Input where your A range ends"))+1,1)]
        bPlus = [*range(int(input("input where your B+ range starts")),int(input("Input where your B+ range ends"))+1,1)]
        b = [*range(int(input("input where your B range starts")),int(input("Input where your B range ends"))+1,1)]
        cPlus = [*range(int(input("input where your C+ range starts")),int(input("Input where your C+ range ends"))+1,1)]
        c = [*range(int(input("input where your C range starts")),int(input("Input where your C range ends"))+1,1)]
        fail = [*range(0,int(input("Input where your failure range ends"))+1,1)]
        gradeDict = [fail,c,cPlus,b,bPlus,a,aPlus]
        return gradeDict,gradeRangeType
    elif gradeRangeType == "none":
        # Taking the range literal of the  user inputs so it can form lists with the grades that are in the range.
        a = [*range(int(input("input where your A range starts")),int(input("Input where your A range ends"))+1,1)]
        b = [*range(int(input("input where your B range starts")),int(input("Input where your B range ends"))+1,1)]
        c = [*range(int(input("input where your C range starts")),int(input("Input where your C range ends"))+1,1)]
        fail = [*range(0,int(input("Input where your failure range ends"))+1,1)]
        gradeDict = [fail,c,b,a]
        return gradeDict,gradeRangeType
# Takes the returns of the other function, and has multiple if paths for the different types of grade ranges and for x in the range of the user input repeats 
# what the grade of the class is then returns it for later use. 
def classGradeFx():
    # takes gradeRange function and returns it into two different variables, 
    usefulInfo = gradeRange()
    gradeDict = usefulInfo[0]
    gradeRangeType = usefulInfo[1]
    classNumber = int(input("How many classes do you have for this grade range type?"))+1
    if classNumber >= 1 and gradeRangeType == "plus-minus" or gradeRangeType == "plusminus" or gradeRangeType == "plus minus" or gradeRangeType == "plus/minus":
        # for x in range of classNumber repeats the code below
        for x in range(classNumber):
            # if grade is in the index of gradeDict, returns letter grade as a new value. 
            letterGrade = float(input("Please enter your grade here without the percentage sign"))
            if letterGrade in gradeDict[0]:
                letterGrade = "FAIL"
                return letterGrade
            elif letterGrade in gradeDict[1]:
                letterGrade = "C-"
                return letterGrade
            elif letterGrade in gradeDict[2]:
                letterGrade = "C"
                return letterGrade
            elif letterGrade in gradeDict[3]:
                letterGrade = "C+"
                return letterGrade
            elif letterGrade in gradeDict[4]:
                letterGrade = "B-"
                return letterGrade
            elif letterGrade in gradeDict[5]:
                letterGrade = "B"
                return letterGrade
            elif letterGrade in gradeDict[6]:
                letterGrade = "B+"
                return letterGrade
            elif letterGrade in gradeDict[7]:
                letterGrade = "A-"
                return letterGrade
            elif letterGrade in gradeDict[8]:
                letterGrade = "A"
                return letterGrade
            elif letterGrade in gradeDict[9]:
                letterGrade == "A+"
                return letterGrade
    elif classNumber >= 1 and gradeRangeType == "plus": 
        # for x in range of classNumber repeats the code below
        for x in range(classNumber):
            letterGrade = float(input("Please enter your grade here without the percentage sign"))
            # if grade is in the index of gradeDict, returns letter grade as a new value. 
            if letterGrade in gradeDict[0]:
                letterGrade = "FAIL"
                return letterGrade
            elif letterGrade in gradeDict[1]:
                letterGrade = "C"
                return letterGrade
            elif letterGrade in gradeDict[2]:
                letterGrade = "C+"
                return letterGrade
            elif letterGrade in gradeDict[3]:
                letterGrade = "B"
                return letterGrade
            elif letterGrade in gradeDict[4]:
                letterGrade = "B+"
                return letterGrade
            elif letterGrade in gradeDict[5]:
                letterGrade = "A"
                return letterGrade
            elif letterGrade in gradeDict[6]:
                letterGrade == "A+"
                return letterGrade
    elif classNumber >= 1 and gradeRangeType == "none":
        # for x in range of classNumber repeats the code below
        for x in range(classNumber):
            letterGrade = float(input("Please enter your grade here without the percentage sign"))
            # if grade is in the index of gradeDict, returns letter grade as a new value. 
            if letterGrade in gradeDict[0]:
                letterGrade = "FAIL"
                return letterGrade
            elif letterGrade in gradeDict[1]:
                letterGrade = "C"
                return letterGrade
            elif letterGrade in gradeDict[3]:
                letterGrade = "B"
                return letterGrade
            elif letterGrade in gradeDict[5]:
                letterGrade = "A"
                return letterGrade
    elif classNumber < 1: 
        # while class number is less than one repeats code.
        while classNumber < 1:
            classNumber = int(input("How many classes do you have for this grade range type?"))+1


# Main starts here:
print(classGradeFx())
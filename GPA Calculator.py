# by Nicholas Walters
# 1/07/2017, Semester 2 2017
# Version 1.0
# 22243339@student.uwa.edu.au

unitCount = int(input("How many completed units have you done (of credits 6)? "))
marks = []
#make a list storing the all of the marks/percent scores
for year in range(unitCount):
    tempMark = int(input("Enter a unit mark: "))
    marks.append(tempMark)
    # for each mark entered, put it in the list of marks (with max number of scores being unitCount)
sum = 0
for mark in marks:
    sum = sum + (mark * 6)
    # sum up all the unit marks in the list, and store value in the sum variable

sumCreditPoints = (unitCount * 6)

WAM = sum / sumCreditPoints
WAM = round(WAM, 2)

# WAM calculation according to UWA. Sum of all marks divided by sum of credit point sum

HD = 0
D = 0
CR = 0
P = 0
F = 0
# variables storing amounts of High Distinctions, Distinctions etc
# Start GPA Calculation

for mark in marks:
    if(mark >= 80):
        HD = HD +1
    if(mark >= 70) and (mark < 80):
        D = D + 1
    if(mark >=60) and (mark < 70):
        CR = CR + 1
    if(mark >=50) and (mark <60):
        P = P + 1
    if(mark < 50):
        F = F + 1
# iterate/scan through all the marks provided in the list
# if the mark in list is above or equal to 80, then increment/add to HD variable count.... etc

Unitsum = (6 * 7 * HD) + (6 * 6 * D) + (6 * 5 * CR) + (6 * 4 * P)
# HD's are valued at 7 points, while D's are 6, CR is 5, Pass is 4
Creditsum = (HD + D + CR + P + F) * 6
# re-calculating the sum of credits (credit points of 6 is assumed)
GPA = Unitsum / Creditsum
GPA = round(GPA, 2)
print()
print("Your UWA GPA is: " + str(GPA))
print("Your UWA WAM is: " + str(WAM))
# convert integer to String, to display the value with a print line
fin = str(input("Press enter to close program: "))
# dummy line
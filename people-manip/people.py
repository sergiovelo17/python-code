class People():
    def __init__(self,ssn,fName,lName,dob,state):
        self.ssn = ssn
        self.fName = fName
        self.lName = lName
        self.dob = dob
        self.state = state
        

def readPeople(l1,nameOfFile):
    peopleFile = open(nameOfFile,"r")
    if peopleFile.mode == 'r':
        contents = peopleFile.readlines()
    for x in contents:
        allWords = x.split(' ')
        l1.append(People(allWords[0],allWords[1],allWords[2],allWords[3],allWords[4]))
    findOldest(l1)

def findOldest(l1):
    oldestPerson = l1[0]
    indexOfOldest = 0
    i = 0
    for x in l1:
        if(x.dob < oldestPerson.dob):
            oldestPerson = x
            indexOfOldest = i
        i += 1
    #swap first and oldest to promote the oldest
    temp = l1[indexOfOldest]
    l1[indexOfOldest] = l1[0]
    l1[0] = temp
    print("The oldest person in the list is: " + oldestPerson.fName + " " + oldestPerson.lName + ", DoB: " + oldestPerson.dob + " State: " + oldestPerson.state + " SSN: " + oldestPerson.ssn)
    print(l1[0].fName)

def printAll(l1):
    for x in l1:
        print(x.fName + " " + x.lName)

def findThemByName(name,l1):
    for x in l1:
        if(x.fName.lower() == name.lower() or x.lName.lower() == name.lower()):
            print(x.fName + " " + x.lName + ": " + x.dob + ", " + x.ssn)



print("Welcome to the People Processing Operator")
answer = raw_input("Which file would you like to read from?: ")
peopleList = []
readPeople(peopleList,answer)
name = raw_input("What name do you want to search?: ")
findThemByName(name,peopleList)

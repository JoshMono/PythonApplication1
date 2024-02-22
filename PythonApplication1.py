import random
import time
import os

def RandomNumber(Amount):
    myNum = random.randint(1, Amount)
    return myNum


def Start():
    userNumber = input("How Many Sides On A Dice Would You Like?: ")
    print("\n\n")
    test = True
    while test:
        try:
            userNumber = int(userNumber)
            test = False
        except:
            userNumber = input("Please Type A Number?: ")
            
    numberList = []
    percentageList = []
    tempList = []
    
    while True:
        
        answerThing = input("Click Enter To Roll (q to restart) or (c to clear): ")
        
        if answerThing == '':
            numberOfSides = userNumber
            number = RandomNumber(userNumber)
            numberList.append(number)
            print(f"Your Roll Is {number} \n \n")
            
        
        elif answerThing == 'q':
            print("\n"*100)
            Start()
            break
        

        elif answerThing == 'c':
            print("\n"*100)
            

        elif answerThing == 'p':
            for i in range(userNumber):
                if numberOfSides == 0:
                    break
                
                for c in (numberList):
                    if c == numberOfSides:
                        tempList.append(c)
                
                
                percentageList.append(len(tempList))
                tempList = []
                numberOfSides = numberOfSides - 1
                
            finalList = []
    
            for i in range(userNumber):
                if i - 1 == userNumber:
                    break
                
                amountOfNumbers = len(numberList)
                
                a = percentageList[i]/amountOfNumbers
                
                a = a*100
                a = round(a)


                finalList.append(a)
                

            for i in range(userNumber):
                print(f"{userNumber-i}. {finalList[i]}%")
                
            finalList = []
            numberList = []
            percentageList = []
            tempList = []
                
                
            
        
        
                
                    
                
                    
                    
                                
        
        
        
Start()



    
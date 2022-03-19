from calendar import firstweekday
import pickle 
import json
# Write a short Python script which queries the user for input 
# (infinite loop with exit possibility) and writes the input to the user
waitingForInput = True
textToBeInputedList = []

def getUserChoice():
    userChoice = input('Please choose option:')
    return userChoice  


def getUserInput():
    userInput = str(input('Please enter text:'))
    return userInput

# Json solution
# def fileManipulation(actionToBeTaken, userInput):
#     with open('File.txt', mode= actionToBeTaken) as f:
#             if actionToBeTaken == 'w':
#                 f.write(json.dumps(userInput))
#             elif actionToBeTaken == 'r':
#                 fileContent = json.loads(f.read())
#                 for line in fileContent:
#                     print(line)
            
# Pickle soluion
def fileManipulation(actionToBeTaken, userInput):
    with open('File.p', mode= actionToBeTaken) as f:
            if actionToBeTaken == 'wb':
                f.write(pickle.dumps(userInput))
            elif actionToBeTaken == 'rb':
                fileContent = pickle.loads(f.read())
                for line in fileContent:
                    print(line)
                    

while waitingForInput:
    print('Which action you want to perform ?')
    print('1: Save text to the file')
    print('2: Print text to the console')
    print('q: Exit')
    userChoice = getUserChoice()
    if userChoice == 1:
        textToBeInputed = getUserInput()
        textToBeInputedList.append(textToBeInputed)
        fileManipulation('wb', textToBeInputedList)
    if userChoice == 2:
        # Add another option to print('1')your user interface: The user should be able to 
        # output the data stored in the file in the terminal
        fileManipulation('rb', None)
    if userChoice == 'q':
        waitingForInput = False


# while waitingForInput:
#     print('Which action you want to perform ?')
#     print('1: Save text to the file')
#     print('2: Print text to the console')
#     print('q: Exit')
#     userChoice = getUserChoice()
#     if userChoice == 1:
#         textToBeInputed = getUserInput()
#         textToBeInputedList.append(textToBeInputed)
#         fileManipulation('w', textToBeInputedList)
        
#     if userChoice == 2:
#         # Add another option to print('1')your user interface: The user should be able to 
#         # output the data stored in the file in the terminal
#         fileManipulation('r', None)
#     if userChoice == 'q':
#         waitingForInput = False


print('Program closed')


# Store user input in a list (instead of directly adding it to the file) 
# and write that list to the file - both pickle and json

# Adjust the logic to load the file content to work with pickled/ json data

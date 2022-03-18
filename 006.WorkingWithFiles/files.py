# Creating new file accessible for writing
f = open('demo.txt', mode = 'w')
f.write('Hello from Python!')
# Force to write information to the file befor getting the input
f.close()

# Getting the input
userInput = input('Please enter input: ')
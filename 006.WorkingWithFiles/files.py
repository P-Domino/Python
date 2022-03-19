# # Creating new file accessible for writing
# f = open('demo.txt', mode = 'w') # w - is overwriting all the time if we want to save content of the file we need to use append - a
# f.write('Hello from Python!')
# # Force to write information to the file befor getting the input
# f.close()

# # Getting the input
# userInput = input('Please enter input: ')

# f = open('demo.txt', mode = 'a ')
# f.write('At this content!\n') # Using line break to create multiline content
# f.close() 

# Reading one line of the document
# f = open ('demo.txt', mode = 'r')
# print(f.readline())
# f.close()

# using with 
with open('demo.txt', mode= 'r') as f: 
    line = f.readline()
    while line: 
        print(line)
        line = f.readline()
print('done!')
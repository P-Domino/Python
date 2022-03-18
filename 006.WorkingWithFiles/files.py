# # Creating new file accessible for writing
# f = open('demo.txt', mode = 'w') # w - is overwriting all the time if we want to save content of the file we need to use append - a
# f.write('Hello from Python!')
# # Force to write information to the file befor getting the input
# f.close()

# # Getting the input
# userInput = input('Please enter input: ')

f = open('demo.txt', mode = 'a ')
f.write('At this content!')
f.close()
# Create a list of names and use a for loop to output the length of each name.
print('-'*10 + '1' + '-'*10)
names = ['Dominik', 'Paul', 'Mery', 'Natali']

for name in names:
    print(name, len(name))

# Adding an if check to print only names longer than 5 characters

print('-'*10 + '2' + '-'*10)

for name in names:
    if len(name) > 5:
        print(name, len(name))

# Adding another if check to see whether a name includes a 'n' or "N" character

print('-'*10 + '3' + '-'*10)

for name in names:
    if len(name) > 5:
        if 'n' in name or 'N' in name:
            print(name, len(name))
    
# Using a while loop to empty list of names

print('-'*10 + '4' + '-'*10)
while names != []:
    names.pop()

print(names)
    
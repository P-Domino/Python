# Create a list of 'Person' dicitionaries with a name, age and list of hobbies for each person.
from operator import index
import random


persons = []
names = ['Dominik', 'Piotr', 'Paul', 'Anna', 'Natalia', 'Paulina']
age = [18, 22, 23, 34, 45, 50]
hobbies = ['Programming', 'gymnastic', 'English', 'Gardening', 'Art']
newDictionary = {}
hobbyNo = random.randrange(0, 5)
def dictionaryCreator(name, age, hobbiesList):
    newDictionary = {
        'name': str(name),
        'age': int(age),
        'hobbies': hobbiesList
    }
    persons.append(newDictionary)


def personSeeder():
    index = 0
    while index < len(names):
        dictionaryCreator(names[index], age[index], hobbies[0:5])
        index += 1
    
personSeeder()
print(persons)

# Use a list comperhension to convert this list of persons into a list of names
personName = [person['name'] for person in persons]
print(personName)

# Use a list comperhension to check whether all persons are older than 20.
personAge = [person['age'] for person in persons if age > 20]
print(personAge)

# copy the person list such that you can safely edit name of the first person
personCopy = [person.copy() for person in persons]
personCopy[0]['name'] = 'Krzysztof'
print(personCopy[0])
print(persons[0])

# Unpack the persons of the orginal list into different variables and output these variables

p1 = persons[0]
p2 = persons[1]
p3 = persons[2]
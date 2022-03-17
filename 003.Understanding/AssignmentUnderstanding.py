# Create a list of 'Person' dicitionaries with a name, age and list of hobbies for each person.
person = []
names = ['Dominik', 'Piotr', 'Paul', 'Anna', 'Natalia', 'Paulina']
age = []
hobbies = ['Programming', 'gymnastic', 'English', 'Gardening', 'Art']
newDictionary = {}

def dictionaryCreator(name, age, hobbiesList):
    newDictionary = {
        'name': str(name),
        'age': int(age),
        'hobbies': hobbiesList
    }
    person.append(newDictionary)
def personSeeder():
    for name in names:
        dictionaryCreator(names[name], age[name], hobbies[name])
    else:
        print(person)
print(age)
print(person)
dictionaryCreator(names[0], 22, hobbies[0:2])
personSeeder()
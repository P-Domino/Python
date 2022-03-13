"""
Assignment
1. Create Two variables - one with your name and one with your age
2. Create a function which prints your data as one string
3. Create a function which prints ANY data (two arguments) as one string
4. Create a function which calculates and returns the number of decades you already lived 
"""

#1
name = 'Dominik'
age = 22

#2
def personal_data():
    person = name + " " + str(age)
    print(person)


personal_data()

#3
def get_personal_data(get_name, get_age):
    person = get_name + " " + str(get_age)
    print(person)

 
get_personal_data("Natalia", 20)

#4
def decades_lived_counter(get_age, decade = 10):
    amount_of_decades_lived = int(get_age) // decade
    print(amount_of_decades_lived)


decades_lived_counter(age)
decades_lived_counter(24)
decades_lived_counter(12.5)
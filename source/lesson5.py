
import random

# For loop
students = ['Ari', 'Anya', 'Ben', 'Gia', 'Yuvi', 'Shraddha', 'Tista',
        'Auyona', 'Evaan']
print('The students:')
print(students)

students.sort()
print('\nThe students sorted by first name:')
print(students)

random.shuffle(students)
print('\nThe students after shuffling:')
print(students)

# Here for and in are keywords, they are in purple
# The syntax: for something in something:
# Here we are iterating over a list, also called list iteration
for st in students:
    print('This prestigious bachelors degree is awarded to: ' + st)
    
for ss in students:
    print(ss + ' gets this degree')
    
for tt in students:
    print('Note: ' + tt + ' gets this degree')
    
# Range for loop
list(range(1, 10))
list(range(10))
list(range(-2, 4))

# This is called iterating over a range
for ir in range(5):
    print('This iteration is ' + str(ir))
    
# Iterating over a dictionary
favorite = {
'Ari': 'Dosa',
'Anya': 'Salad',
'Gia': 'Cheese',
'Yuvi': 'Samosa', 
'Shraddha': 'Pau Bhaji', 
'Tista': 'Ice cream',
'Auyona': 'Phoochka', 
'Evaan': 'Samosa'
}

# '.' is a operator that's used to call functions on a 'class' or 
# from a 'module' or an 'object' of a 'class'
# Note: the print function can take multiple arguments
for Name, Food in favorite.items():
    print(Name, Food)
    
for name, food in favorite.items():
    print('The favorite food of ' + name + ' is ' + food)
    
    
    


    
    
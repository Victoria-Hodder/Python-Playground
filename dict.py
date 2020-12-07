my_dict = {'fruit': 'apple', 'animals': 'bat', 'books': 42}
# print(my_dict)

# for key in my_dict.keys():
#     print(key)

# for value in my_dict.values(): 
#     print(value)

my_dict2 = {'age': 31, 'no_of_coffees': 2}
# print(my_dict2)
my_dict2['no_of_coffees'] = 4
# print(my_dict2)
# print(my_dict2['no_of_coffees'])

names = ["Lola", "Mary", "Sissi"]
grades = [23, 34, 45]

# Dictionary comprehension to create dict from names and grades
print({n:g for n,g in zip(names,grades)})

students = [{'name': 'Mary', 'grade': 4}, {'name': 'Sissi', 'grade': 19}, {'name': 'Frank', 'grade': 14}]

# List comp to create list of grades from students
grades = [s['grade'] for s in students]
print(grades)

# If loop within list comp to print GRADES if above certain threshold
grades = [s['grade'] for s in students if s['grade'] > 10]
print(grades)

# If loop within list comp to print NAMES if above certain threshold
grades = [s['name'] for s in students if s['grade'] > 10]
print(grades)
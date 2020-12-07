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
all_grades = [s['grade'] for s in students]
print(f"Print all grades: {all_grades}")

# If loop within list comp to print GRADES if above certain threshold of 10
passing_grades = [s['grade'] for s in students if s['grade'] > 10]
print(f"Passing grade(s): {passing_grades}")

# If loop within list comp to print NAMES if above certain threshold of 10
passing_students = [s['name'] for s in students if s['grade'] > 10]
print(f"Student name(s) with passing grade: {passing_students}")

# Print NAME of students whose grades are divisible by 2 AND above threshold of 10
grades_mod2 = [s['name'] for s in students if s['grade']%2==0 if s['grade'] > 10]
print(f"Student names(s) with passing grade divisible by two: {grades_mod2}")
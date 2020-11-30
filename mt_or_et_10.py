"""
Write a function that gets a list of numbers and prints the 
numbers that are more or equal to 10. eg. passing([1, 2, 3, 10, 11, 4, 18)
"""

def return_greater(numbers, threshold):
    for num in numbers:
        if num >= threshold:
            print(num)

# return_greater([1, 2, 3, 10, 11, 4, 18], 15)
# print()
# return_greater([52, 2, 13, 60, 11, 48, 8], 50)


"""
A. Given a list with dictionaries of the form [{'name': 'Mary', 'grade': 4}, 
{'name': 'Sissi', 'grade': 19}] and a threshold number, make a function to return 
a list of dictionaries with the student that have grade more than the number.

B. On top of the A solution. Use that function to get the passing students. Then 
print the passing students names (not inside the function of A, after it is used).

"""

# return list of dictionaries
def return_dictlist(thisdictlist):
   for value in enumerate(thisdictlist):
      print(value)

return_dictlist([{'name': 'Mary', 'grade': 4}, {'name': 'Sissi', 'grade': 19}])

# return key-value pair of students who have a grade higher than threshold
def return_passgrades(thisdictlist, threshold):
    for value in thisdictlist:
        if value['grade'] >= threshold:
            print(f"{value['name']} passed with score {value['grade']}")

return_passgrades([{'name': 'Mary', 'grade': 4}, {'name': 'Sissi', 'grade': 19}, {'name': 'Frank', 'grade': 14}], 15)

return_passgrades([{'name': 'Mary', 'grade': 4}, {'name': 'Sissi', 'grade': 19}, {'name': 'Frank', 'grade': 14}], 20)

return_passgrades([{'name': 'Mary', 'grade': 4}, {'name': 'Sissi', 'grade': 19}, {'name': 'Frank', 'grade': 14}], 5)

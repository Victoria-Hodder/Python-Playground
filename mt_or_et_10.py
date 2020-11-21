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


1. Learn to print key, value pairs from dictionaries
2. print list of dicts
3. threshold number

B. On top of the A solution. Use that function to get the passing students. Then 
print the passing students names (not inside the function of A, after it is used).

"""

def return_dictlist(thisdictlist):
    for key, value in enumerate(thisdictlist):
        print(f"{value['name']} - {value['grade']}")


return_dictlist([{'name': 'Mary', 'grade': 4}, {'name': 'Sissi', 'grade': 19}])

# Output:
# Mary : 4
# Sissi : 19
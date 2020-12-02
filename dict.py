my_dict = {'fruit': 'apple', 'animals': 'bat', 'books': 42}
print(my_dict)

for key in my_dict.keys():
    print(key)

print()

for value in my_dict.values():
    print(value)

print()

my_dict2 = {'age': 31, 'no_of_coffees': 2}
print(my_dict2)
my_dict2['no_of_coffees'] = 4
print(my_dict2)
print(my_dict2['no_of_coffees'])
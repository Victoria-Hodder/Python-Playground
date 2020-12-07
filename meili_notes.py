# thisdict = {'name': 'Mary', 'grade': 4} 

# Prints out the key and value from thisdict variable on separate lines
# for key in thisdict:
#     print(thisdict[key])


# Prints key, value pair from thisdict argument
def return_dict(thisdict):
    for x, y in thisdict.items():
        print(x, " : ", y)

return_dict([{'name': 'Mary', 'grade': 4}, {'name': 'Sissi', 'grade': 19}])
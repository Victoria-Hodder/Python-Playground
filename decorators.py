def decorator_list(fnc):
    def inner(list_of_tuples):
        return [fnc(val[0], val[1]) for val in list_of_tuples]
    return inner

@decorator_list
def add_together(a,b):
    return a + b

print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))



def meta_decorator(arg):
    def decorator_list(fnc):
        def inner(list_of_tuples):
            return [(fnc(val[0], val[1])) ** power for val in list_of_tuples]
        return inner
    if callable(arg):
        power = 2
        return decorator_list(arg)
    else:
        power = arg
        return decorator_list

# What is this if statment doing? If there is no arguments in the decoator 
# then it accepts the default (in this case 2), if you give an argument then 
# it accepts this argument instead

@meta_decorator(3)
def add_together(a,b):
    return a + b

print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))

# Source: 
# https://towardsdatascience.com/how-to-use-decorators-in-python-by-example-b398328163b
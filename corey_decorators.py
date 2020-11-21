""" 
Building knowledge of decorators
Resources: 
https://www.youtube.com/watch?v=FsAPt_9Bf3U&list=WL&index=14
https://www.programiz.com/python-programming/decorator


"""


def decorator_function(original_function):
    def wrapper_function():
        original_function()
        print('here is the wrapper function')
    return wrapper_function

@decorator_function
def display():
    print('display function ran')

def display2():
    print('display2 ran without decorator')

display()
display2()
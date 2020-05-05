""" 
Building knowledge of decorators
Resource: https://www.youtube.com/watch?v=FsAPt_9Bf3U&list=WL&index=14

"""

def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)
    return inner_function()

outer_function()
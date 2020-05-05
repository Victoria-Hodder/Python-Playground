""" 
Building knowledge of decorators
Resource: https://www.youtube.com/watch?v=FsAPt_9Bf3U&list=WL&index=14

"""

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function()

@decorator_function
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print(f'display_info ran with arguments {name} {age}')


display_info('Victoria', 92)

print(display)
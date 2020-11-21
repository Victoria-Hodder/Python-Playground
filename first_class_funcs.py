def square(x):
    return x * x

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
# print(squares)

cubes = my_map(cube, [1, 2, 3, 4, 5])
# print(cubes)

""" wrapper function """

def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}<{tag}>')
    return wrap_text

# print_h1 = html_tag('h1')
# print_h1('Test Headline')
# print_h1('Another headline')

# print_p = html_tag('p')
# print_p('Test paragraph')


def greetings(salutation):
    def humanity(globe):
        print(f'{salutation}, {globe}!')
    return humanity

print_hello = greetings('Hello')
print_hello('World')



""" Closures """

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


times3 = make_multiplier_of(3)
print(times3(4))
print(times3.__closure__[0].cell_contents)

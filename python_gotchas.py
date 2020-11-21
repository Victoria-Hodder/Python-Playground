"""
Resource: https://docs.python-guide.org/writing/gotchas/
"""

def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to

my_list = append_to(12)
print(my_list)

my_other_list = append_to(42)
print(my_other_list)
numbers = range(10)
new_dict_for = {}

"""Add values to `new_dict` using for loop"""
for n in numbers:
    if n%2==0:
        new_dict_for[n] = n**3

print(new_dict_for)

new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}

print(new_dict_comp)


""" Converting fahrenheit into celsius """

fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

# Using lambda function to convert celsius to fahrenheit
# Using round to limit float digits
celsius = list(map(lambda x: round((float(5)/9)*(x-32)), fahrenheit.values()))

#Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))

print(celsius_dict)

# The same but as a dict comprehension
celsius_dict_comp = {k:round((float(5)/9)*(v-32)) for (k,v) in fahrenheit.items()}

print(celsius_dict_comp)

"""Dict comprehension with conditional"""

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Check for items greater than 2 and modulus 2
dict1_cond = {k:v for (k,v) in dict1.items() if v>2 if v%2==0}

print(dict1_cond)

""" if else """

dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}

# Identify odd and even entries
dict2_tripleCond = {k:('even' if v%2==0 else 'odd') for (k,v) in dict2.items()}

print(dict2_tripleCond)

"""
Source:
https://www.datacamp.com/community/tutorials/python-dictionary-comprehension?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=m&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=229765585186&utm_targetid=aud-763347114660:dsa-473406574715&utm_loc_interest_ms=&utm_loc_physical_ms=9061132&gclid=Cj0KCQiAzZL-BRDnARIsAPCJs724VDgvfY4DuG9sbkGKilmH2ArA_pyrGh0i9l7lqIIhd6Ah8JpzvGAaAtIJEALw_wcB#pdc
"""
import math

""" Arrows """

# thickness = 7
# c = '*'

# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


""" Heart """

# c='*'
# width = 40

# print ((c*2).center(width//2)*2)

# for i in range(1,width//10+1):
#     print (((c*int(math.sin(math.radians(i*width//2))*width//4)).rjust(width//4)+
#            (c*int(math.sin(math.radians(i*width//2))*width//4)).ljust(width//4))*2)

# for i in range(width//4,0,-1):
#     print ((c*i*4).center(width))
# print ((c*2).center(width))


""" welcome mat """

# n, m = 21, 63

# # n is odd number, m is 3*n

# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['HELLO, WORLD!'.center(m, '-')] + pattern[::-1]))

# #same design - different code

N = 9
M = 27 
design1 = "-" 
design2 = ".|." 
design3 = "WELCOME" 
line = [] 

def print_sy(strt , range_, stp): 
    for i in range(strt,range_,stp): 
        line.append(((M-(2*i+1)*3)//2)*design1 + (2*i+1)*design2 + ((M-(2*i+1)*3)//2)*design1) 
        print(line[i])

print_sy(0,(N-1)//2,1) 
print((M-7)//2 *design1 +design3 + (M-7)//2 *design1) 
print_sy((N-2)//2,-1,-1)
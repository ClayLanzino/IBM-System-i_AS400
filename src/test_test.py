# -*- coding: utf-8 -*-

""" Python Scripts to testing out some Python functions in order to know how is it work """

# Defining a lis with 12 elements ...
lis = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
       'December']

# Printing teh entering list ...
print('Printing entering list', lis)
print()

# Printing the list in inverting order mode ...
print('Printing the list in inverting order', lis[::-1])
print()

# Printing, how many elements does the list have?
print('The length list is --->', len(lis), 'Elements')
print()

# Printing just the first and last elements ...
print('The first element in the list is ...->', lis[0])
print()

# Printing just the last elements in the list ...
print('Printing the last element in the list ->', lis[11])
print()

# For, looping to print all elements of the list in vertical way ...
for i in lis:
    print('Printing ...', i)
print()

""" lis = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
       'December']   
 It is also possible to access a part of a list, by indicating (optionally) from the start index to the end index: """
# Printing in slices
print(lis[1:4])  # Returns: 'February', 'March', 'April',
print(lis[3:])   # Returns: 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
print(lis[:2])   # Returns: 'January', 'February'


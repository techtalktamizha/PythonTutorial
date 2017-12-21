# List syntax
# [x,x,x,x,x,[y,y,y],'value']
l1 = list(range(10))
l2 = list(range(10,30))

# Printing List
# print(l1)
# print(l2)
# Adding values to List
# l1.append('Testing')
# print(l1)
# Add values at specified position
# l1.insert(3, '4th Position')
# print(l1)
# Extending List
# l1.append(l2)
# l1.extend(l2)
# Delete from list
# l1.pop(5)
# Find the index
# print(l1.index(5)+1)
# Copy all content from another List
# l3 = l1.copy()
# print(l3)
# Count the occurences of value in List
# l1.append(4)
# print(l1.count(4))
# Reverse the list
# l1.reverse()
# Sort the list
# l1.sort()
# Clear the List
# l1.clear()
# zip the lists
zipped = zip(l1, l2)
print(l1)
print(l2)
print([x for x in zipped])
import sys
print(sys.version)
'''
values = range(100)
evens = []
for no in values:
	if no%2 == 0:
		evens.append(no)
print(evens)
print([no for no in values if no%2 == 0 ])
'''
dictcomp = {x:x*3 for x in "arockia"}
setcomp = {x for x in [1,2,3,3]}
print(dictcomp)
print(setcomp)

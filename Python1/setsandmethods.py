set1 = {1,2,8,4,6} # Immutable
set2 = {6,7,8,9,10}
setempty = set()
# print(set1.pop()) # removing random element in set1
# print(set1.clear()) # Clearing set1
# print(set1.add(10)) # Adding Element in set1
print(set1.union(set2)) # Union combine all element without common element
print(set1.intersection(set2)) # common element

print(set1)
print(set2)
print(setempty, type(setempty))

''' dict1 = {} # Empty Dictionary and Mutable
dict2 = {}
print(type(dict1))
print(type(dict2))
print(dict1 , type(dict1)) '''

dict1 = {"Good": "Joy", "Junaid": "Malik", "Help": "me"}
marks = {"junaid": "84", "malik": "67", "idrees": "90"}
marks2 = {"junaid": 84, "malik": 67, "idrees": 90}  # marks = {"keys" : values}
print(marks["junaid"])
print(marks2["malik"])
marks["Arif"]= 89 # adding
print(marks.get("junaid malik")) # fetching data and not showing error
print(marks.get("junaid"))
print(marks["junaid"]) # another way fetching value and showing error
print(marks)
print(marks.keys()) # showing keys
print(marks.values()) # showing values
print(marks.items()) # showing items

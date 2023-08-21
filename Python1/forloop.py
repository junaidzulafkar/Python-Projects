'''a = int(input("Which table you want print: "))
i = int(input("enter range: "))
for i in range(i):
    print(a,"*",i,"=",a*i)'''

'''print("printing List")
a = [1,2,3,4,5,6,7]
b = {9,8,7,6,5,4,13}

for item in a:
    print(item)
print(type(a))
print("printing Set")
for item2 in b:
    print(item2)
print(type(b))
'''

for j in range(5):
    if (j == 3):  # Breaking Loop
        break
    print(j + 1)
print("Excution Complete...")

for j in range(5):
    if (j == 3):  # Skipping Number 4
        continue
    print(j + 1)
print("Excution Complete...")

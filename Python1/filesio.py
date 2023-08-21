# Write File
s = "Hi, Junaid Malik"
with open("junaid.txt","w") as f:
    f.write(s)
    f.close()

# Read File

'''with open("junaid.txt","r") as f:
    s = f.read()
    print(s)'''

# Or Read File

'''f = open("junaid.txt","r")
s = f.read()
print(s)'''

# Append File
'''a = open("junaid.txt","a")
a.write(" maliks")'''

   # Or

'''with open("junaid.txt","a") as a:
    a.write("Idrees")'''
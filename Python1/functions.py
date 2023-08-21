'''def hello():
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print("hello")
hello()
print("exit")'''

'''def hello():
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print("hello")


print("Execution Start")
hello()
print("exit")'''

def hello(name, ending):
    print("hello" + name)
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print(ending)

def lettergenerator(name,date):
    st = f"Hi mama,\nthis is {name} i am not coming on this {date}"
    print(st)

def average(a,b):
    return (a+b)/2


print("Execution Start")
hello("junaid","thank u")
hello("Idrees","Sorry")
lettergenerator("junaid","20-3-2-2023")
lettergenerator("Idrees","22-3-2-2023")
print(average(2,2))
print("exit")
try:
    a = int(input("Enter Number: "))
    print(a + 3)

except Exception as e:
    print("some error occured: ", e)
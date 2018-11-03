print("python learning sequence #3 | math")
int1 = int(input("Enter integer 1..:"))
int2 = int(input("Enter integer 2..:"))
print("Selections: ")
print("1) int1 + int2 ")
print("2) int1 - int2 ")
print("3) int2 - int1 ")
print("4) int1 * int2 ")
print("5) int1 / int2 ")
print("6) int2 / int1 ")

selection = int(input("select: "))
if selection == 1:
    result = int1+int2
elif selection == 2:
    result = int1-int2
elif selection == 3:
    result = int2-int1
elif selection == 4:
    result = int1*int2
elif selection == 5:
    result = int1/int2
elif selection == 6:
    result = int2/int1
else:
    print("INVALID INPUT")
    quit()
print(result)

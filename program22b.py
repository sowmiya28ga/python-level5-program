print("Right-Aligned Right Triangle Pattern")
print("-----------------------------------")
n = int(input("Enter The Number: "))
for i in range(1, n + 1):
    for space in range(n - i):
        print("  ", end="")  
    for j in range(i):
        print("* ", end="")
    print()

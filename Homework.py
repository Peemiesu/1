num  = int(input("Num: "))
for i in range(1, num + 1):
    print(" " * (num-i), end="")
    for j in range(i):
        print(j + 1, end=" ")
    print()
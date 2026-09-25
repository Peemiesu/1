grid = []
value = 0
count = 0
input_value = input("Input rows and columns: ").split()
int_value = []
for integer in range(len(input_value)):
        int_value.append(int(input_value[integer]))
for i in range(int_value[0]):
    req_met = False
    repeat = False
    while req_met == False:
        if repeat == True:
            print(f"There are {int_value[1]} columns")
        row = input(f"Input the each of the {int_value[1]} column's value on row {i + 1}: ").split()
        if len(row) == int_value[1]:
            req_met = True
        repeat = True
    inted = []
    for num in range(len(row)):
        inted.append(int(row[num]))
    grid.append(inted)
for line in range(len(grid)):
    for columns in range(len(grid[line])):
        if 50 >= grid[line][columns] >= 10 and grid[line][columns]%2 == 0:
            value += grid[line][columns]
            count += 1
print(f"Number of accepted artifacts: {count}\nSum of their values: {value}")
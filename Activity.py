steps = int(input("Enter the number of steps: "))
energy = 0

for step in range(1, steps + 1):
    energy += step
print(f"energy: {energy}")
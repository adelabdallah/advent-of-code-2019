file = open('./day1/input.txt', 'r')
lines = file.read().splitlines()
file.close()

# Part 1

total = 0

for num in lines:
    total += (int(num) // 3) - 2

print(total)

# Part 2

recursiveTotal = 0


def addFuelRecursively(num):
    global recursiveTotal
    amountToAdd = (int(num) // 3) - 2

    if (amountToAdd <= 0):
        return

    recursiveTotal += amountToAdd

    addFuelRecursively(amountToAdd)


for num in lines:
    addFuelRecursively(num)

print(recursiveTotal)

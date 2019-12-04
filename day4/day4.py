
def checkIncreasing(num):
    n = str(num)

    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return False

    return True


def containsDuplicate(num):
    n = str(num)

    for i in range(len(n) - 1):
        if n[i] == n[i + 1]:
            return True

    return False


def containsDuplicatePair(num):
    n = str(num)

    for i in range(len(n) - 1):
        if n[i] == n[i + 1] and n.count(n[i]) == 2:
            return True

    return False


# Part 1

count = 0

for i in range(152965, 670284):
    if checkIncreasing(i) and containsDuplicate(i):
        count += 1

print(count)

# Part 2

count2 = 0

for i in range(152965, 670284):
    if checkIncreasing(i) and containsDuplicatePair(i):
        count2 += 1

print(count2)

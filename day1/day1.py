file = open('./day1/input.txt', 'r')
lines = file.read().splitlines()
file.close()

total = 0

for num in lines:
    total += (int(num) // 3) - 2

print(total)

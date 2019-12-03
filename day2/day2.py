def determineOutput(nums, noun, verb):

    nums[1] = noun
    nums[2] = verb
    loopVar = 0

    while nums[loopVar] != 99:

        cmd = nums[loopVar]
        input1 = nums[nums[loopVar + 1]]
        input2 = nums[nums[loopVar + 2]]
        outputPos = nums[loopVar + 3]

        if cmd == 1:
            nums[outputPos] = input1 + input2
        elif cmd == 2:
            nums[outputPos] = input1 * input2

        loopVar += 4

    print(nums[0])
    return nums[0]


def determineSpecificOutput(nums, target):
    for i in range(100):
        for j in range(100):
            if determineOutput(nums, i, j) == target:
                print(100 * i + j)
                return


# Part 1
file = open('./day2/input.txt', 'r')
addresses = [int(i) for i in file.read().split(",")]
file.close()

determineOutput(addresses, 12, 2)

# Part 2

determineSpecificOutput(addresses, 19690720)


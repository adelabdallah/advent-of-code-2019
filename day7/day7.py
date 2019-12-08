def getParamByMode(mode, step, index, inputs):
    if mode == 0:
        return inputs[inputs[index + step]]
    return inputs[index + step]


def getParamsByMode(mode1, mode2, index, inputs):
    return getParamByMode(mode1, 1, index, inputs), getParamByMode(mode2, 2, index, inputs)


def getParamModes(modes):
    return [int(mode) for mode in [modes[2], modes[1], modes[2], modes[3:]]]


def addition(mode1, mode2, index, inputs):
    param1, param2 = getParamsByMode(mode1, mode2, index, inputs)
    inputs[inputs[index + 3]] = param1 + param2


def multiply(mode1, mode2, index, inputs):
    param1, param2 = getParamsByMode(mode1, mode2, index, inputs)
    inputs[inputs[index + 3]] = param1 * param2


def less(mode1, mode2, index, inputs):
    param1, param2 = getParamsByMode(mode1, mode2, index, inputs)
    inputs[inputs[index + 3]] = 1 if param1 < param2 else 0


def equal(mode1, mode2, index, inputs):
    param1, param2 = getParamsByMode(mode1, mode2, index, inputs)
    inputs[inputs[index + 3]] = 1 if param1 == param2 else 0


def jumpIfTrue(mode1, mode2, index, inputs):
    param1, param2 = getParamsByMode(mode1, mode2, index, inputs)
    return param2 if param1 != 0 else index + 3


def jumpIfFalse(mode1, mode2, index, inputs):
    param1, param2 = getParamsByMode(mode1, mode2, index, inputs)
    return param2 if param1 == 0 else index + 3


def computify(inputs, userInput):
    index = 0
    diagnostic = None
    while inputs[index] != 99:
        mode1, mode2, mode3, opcode = getParamModes(f"{inputs[index]:05}")
        if opcode == 1:
            addition(mode1, mode2, index, inputs)
            index += 4
        elif opcode == 2:
            multiply(mode1, mode2, index, inputs)
            index += 4
        elif opcode == 3:
            inputs[inputs[index + 1]] = userInput
            index += 2
        elif opcode == 4:
            diagnostic = inputs[inputs[index + 1]]
            index += 2
        elif opcode == 5:
            index = jumpIfTrue(mode1, mode2, index, inputs)
        elif opcode == 6:
            index = jumpIfFalse(mode1, mode2, index, inputs)
        elif opcode == 7:
            less(mode1, mode2, index, inputs)
            index += 4
        elif opcode == 8:
            equal(mode1, mode2, index, inputs)
            index += 4

    return diagnostic

with open('./day7/input.txt') as _file:
    for line in _file.readlines():
        line.split(",")
        
        #And that's about as far as I got with this doozy
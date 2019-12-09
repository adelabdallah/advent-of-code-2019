def divideByDimension(rawInput, dimension):
    divided = []
    i = dimension
    j = 0
    while i <= len(rawInput):
        divided.append(rawInput[j:i])
        j = i
        i += dimension

    return divided


def getLayers(rawInput, width, height):
    return divideByDimension(divideByDimension(rawInput, width), height)


def countDigit(strInput, digit):
    return len(strInput) - len(strInput.replace(digit, ""))


def findLeastZeros(layers):
    layerCounts = {}
    for i in range(len(layers)):
        layerCounts[i] = 0
        for j in range(len(layers[i])):
            layerCounts[i] += countDigit(layers[i][j], "0")

    return min(layerCounts, key=layerCounts.get)


def multiplyDigits(rawInput, width, height, digit1, digit2):
    countDigit1 = 0
    countDigit2 = 0

    layer = getLayers(rawInput, width, height)[
        findLeastZeros(getLayers(rawInput, width, height))]

    for i in range(len(layer)):
        countDigit1 += countDigit(layer[i], "1")
        countDigit2 += countDigit(layer[i], "2")

    return countDigit1 * countDigit2


with open('./day8/input.txt') as _file:
    for line in _file.readlines():
        print(multiplyDigits(line, 25, 6, "1", "2"))

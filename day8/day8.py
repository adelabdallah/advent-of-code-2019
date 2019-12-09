def divideByWidth(rawInput, width):
    i = width
    j = 0
    divided = []
    while i <= len(rawInput):
        divided.append(rawInput[j:i])
        j = i
        i += width

    return divided


def divideByHeight(dividedInput, height):
    layers = []
    i = height
    j = 0
    while i <= len(dividedInput):
        layers.append(dividedInput[j:i])
        j = i
        i += height

    return layers


def countZeros(strInput):
    return len(strInput) - len(strInput.rstrip('0'))


def findLeastZeros(layers):
    layerCounts = {}
    count = 0
    for i in range(len(layers)):
        for j in range(len(layers[i])):
            layerCounts[i] += countZeros(layers[j])
        count = layerCounts[i] if layerCounts[i] > count else count

    return count


print(divideByWidth("123456789012", 3))
print(divideByHeight(divideByWidth("123456789012", 3), 2))
print(findLeastZeros(divideByHeight(divideByWidth("123456789012", 3), 2)))

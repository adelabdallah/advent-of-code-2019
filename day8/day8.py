def createLayers(rawInput, width, height):
    layers = []

    for i in range(len(rawInput) + 1):
        layer = []
        for j in range(height + 1):
            layer.append(rawInput[j:width])
            i += width
            width += width

        layers.append(layer)

    return layers


print(createLayers("123456789012", 3, 2))

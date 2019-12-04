def coordinatify(directions):
    currentX = 0
    currentY = 0
    coordinates = []
    for d in directions:
        if d[0] == "R":
            # int(d[1:]) is the number value of the movement
            currentX = currentX + int(d[1:])
            for i in range(int(d[1:]) + 1):
                coordinates.append((i, currentY))
        elif d[0] == "L":
            currentX = currentX - int(d[1:])
            for i in range(int(d[1:]) + 1):
                coordinates.append((i, currentY))
        elif d[0] == "U":
            currentY = currentY + int(d[1:])
            for i in range(int(d[1:]) + 1):
                coordinates.append((currentX, i))
        elif d[0] == "D":
            currentY = currentY - int(d[1:])
            for i in range(int(d[1:] + 1):
                coordinates.append((currentX, i))

    return set(coordinates)


def shortestDistance(coords):
    distances=[]
    for i in coords:
        distances.append(i[0] + i[1] if i[0] + i[1]
                         > 0 else (i[0] + i[1]) * -1)

    return distances


file=open('./day3/input1.txt', 'r')
lines=file.readlines()
file.close()

wire1Directions=lines[0].split(",")
wire2Directions=lines[1].split(",")

wire1Coords=coordinatify(wire1Directions)
wire2Coords=coordinatify(wire2Directions)

intersections=wire1Coords & wire2Coords

shortestDist=shortestDistance(intersections)

print(intersections)
print(shortestDist)
print(sorted(shortestDist)[0])

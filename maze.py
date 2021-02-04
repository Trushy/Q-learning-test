def checkMap(Map):
    Player = 0
    Cheese = 0

    for line in Map:
        if len(Map) != len(line):
            raise Exception("Map isn\'t a square.")
        for char in line:
            if char == 'P':
                Player += 1
            if char == 'C':
                Cheese += 1
            if char != '#' and char != 'X' and char != 'P' and char != 'C':
                raise Exception("Unwanted chars in the map.")
    if Player != 1 or Cheese != 1:
        raise Exception("Too much players or cheeses.")
    return 0

def getMap():
    file = open("map.txt", "r")
    content = file.read()
    Map = content.split('\n')
    checkMap(Map)
    return Map

def createMaze():
    Map = getMap()

    return Map
import itertools

a = ["X..","...","XX."]

def f(x,y,sizeX,sizeY):
    if x == -1 or y == -1 or x == sizeX or y == sizeY:
        return True
    return False

def calculateNeighbours(index, index1, sizeX, sizeY):
    neighborhood = list(itertools.product([index-1, index, index+1], [index1 - 1, index1, index1 + 1]))
    neighborhood.remove((index,index1))
    neighborhood = [el for el in neighborhood if not f(el[0], el[1], sizeX, sizeY)]
    return neighborhood

def minesweeperCalc(data):
    data = [[0 if char == '.' else char for char in el] for el in data]
    print(data)
    n = len(data)
    m = len(data[0])

    for index in range(len(data)):
        for index1 in range(len(data[0])):
            if data[index][index1] == 'X':
                neighborhood = calculateNeighbours(index, index1, n, m)
                for x,y in neighborhood:
                        if data[x][y] !='X':
                            data[x][y]+=1


    return data

print(minesweeperCalc(a))






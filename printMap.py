
class Pipe:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y


pipesList = []
maxX = 0
maxY = 0

f = open("./maintest.txt", 'r', encoding='utf-8')
inpp = 0

for line in f:
    readLine = line.split()
    x = int(readLine[1])
    y = int(readLine[2])
    pipesList.append(Pipe(readLine[0], int(readLine[1]), int(readLine[2])))
    
    if(x > maxX):
        maxX = x
    if(y > maxY):
        maxY = y
f.close()

pipesGraph = []
for i in range(maxX):
    pipeRow = []
    for j in range(maxY):
        pipeRow.append(None)
    pipesGraph.append(pipeRow)

for pipe in pipesList:
    pipesGraph[pipe.x - 1][pipe.y - 1] = pipe

stringRep = ""

for i in range(maxY):
    for pipe in pipesGraph[i]:
        if(pipe == None):
            stringRep += " "
        else:
            stringRep += pipe.value
    print(stringRep)
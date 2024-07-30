

def solution(fileLoca):

    class Pipe:
        def __init__(self, value, x, y):
            self.value = value
            self.x = x
            self.y = y
        
        def getPosition(self):
            return (self.x, self.y)
        
        def pointsTo(self):
            match self.value:
                case '=':
                    return ((self.x - 1, self.y),(self.x + 1, self.y))
                case '║':
                    return ((self.x, self.y - 1),(self.x, self.y + 1))
                case '╔':
                    return ((self.x + 1, self.y),(self.x, self.y - 1))
                case '╗':
                    return ((self.x - 1, self.y),(self.x, self.y - 1))
                case '╚':
                    return ((self.x + 1, self.y),(self.x, self.y + 1))
                case '╝':
                    return ((self.x - 1, self.y),(self.x, self.y + 1))
                case '╠':
                    return ((self.x + 1, self.y),(self.x, self.y - 1),(self.x, self.y + 1))
                case '╣':
                    
                    return ()
                case '╦':
                    return ()
                case '╩':
                    return ((self.x + 1, self.y),(self.x, self.y - 1),(self.x, self.y + 1))
                case _:
                    return ((self.x + 1, self.y),(self.x, self.y - 1),(self.x, self.y + 1))
        
        def isConnected(self, otherPipe):
            match otherPipe.value:
                case '=':
                    if((otherPipe.x - 1 == self.x or otherPipe.x + 1 == self.x) and otherPipe.y == self.y):
                        return True
                case '║':
                    if((otherPipe.y -1 == self.y or otherPipe.y + 1 == self.y) and otherPipe.x == self.x):
                        return True
                case '╔':
                    if((otherPipe.y - 1 == self.y and otherPipe.x == self.x) or (otherPipe.x + 1 == self.x and otherPipe.y == self.y)):
                        return True
                case '╗':
                    if((otherPipe.y - 1 == self.y and otherPipe.x == self.x) or (otherPipe.x - 1 == self.x and otherPipe.y == self.y)):
                        return True
                case '╚':
                    if((otherPipe.y + 1 == self.y and otherPipe.x == self.x) or (otherPipe.x + 1 == self.x and otherPipe.y == self.y)):
                        return True
                case '╝':
                    if((otherPipe.y + 1 == self.y and otherPipe.x == self.x) or (otherPipe.x - 1 == self.x and otherPipe.y == self.y)):
                        return True
                case '╠':
                    if(((otherPipe.y + 1 == self.y or otherPipe.y - 1 == self.y) and otherPipe.x == self.x) or (otherPipe.x + 1 == self.x and otherPipe.y == self.y)):
                        return True
                case '╣':
                    if(((otherPipe.y + 1 == self.y or otherPipe.y - 1 == self.y) and otherPipe.x == self.x) or (otherPipe.x - 1 == self.x and otherPipe.y == self.y)):
                        return True
                case '╦':
                    if((otherPipe.y - 1 == self.y and otherPipe.x == self.x) or ((otherPipe.x - 1 == self.x or otherPipe.x + 1 == self.x) and otherPipe.y == self.y)):
                        return True
                case '╩':
                    if((otherPipe.y + 1 == self.y and otherPipe.x == self.x) or ((otherPipe.x - 1 == self.x or otherPipe.x + 1 == self.x) and otherPipe.y == self.y)):
                        return True
                case _:
                    if(((otherPipe.y + 1 == self.y or otherPipe.y - 1 == self.y) and otherPipe.x == self.x) or ((otherPipe.x + 1 == self.x or otherPipe.x - 1 == self.x) and otherPipe.y == self.y)):
                        return True
            return False
        def toString(self):
            return "{" + self.value + "," + str(self.x) + "," + str(self.y) + "}"

                
    file = open(fileLoca, "r", encoding='utf-8')

    pipeMap = []
    startingPipe = None

    #reads file line by line
    for line in file:
        read = line.split()
        pipeMap.append(Pipe(read[0], int(read[1]), int(read[2])))
        if(read[0] == '*'):
            startingPipe = pipeMap[-1]

    file.close()

    #looks for connections
    seenPipes = set()

    def depthFirstSearch(visited, pipe):
        visited.add(pipe)
        for traverse in pipeMap:
            if(traverse not in visited):
                if(pipe.isConnected(traverse)):
                    print("pipe " + pipe.toString() + " is connected to " + traverse.toString())
                    depthFirstSearch(visited, traverse)

    depthFirstSearch(seenPipes, startingPipe)

    sortedPipes = ''

    for pipe in seenPipes:
        if(pipe.value.isalpha()):
            sortedPipes += pipe.value
    print(''.join(sorted(sortedPipes)))

solution("./maintest.txt")
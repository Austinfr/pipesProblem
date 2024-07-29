def solution(input):
    #open file
    file = open(input, "r", encoding='utf-8')

    startingPoint = []

    #create grid representation
    pipeGrid = {}

    #read file
    for line in file:
        pipeData = line.strip().split()
        x = pipeData[1]
        y = pipeData[2]
        pipeGrid[(x, y)] = pipeData[0]
        if(pipeData[0] == '*'):
            startingPoint = [pipeData[1], pipeData[2]]

    print(pipeGrid)
        

    def dfs(grid, startX, startY):
        rows, cols = len(grid), len(grid[0])
        stack = [(startX, startY)]
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        while stack:
            x, y = stack.pop()

            if not (0 <= x < cols and 0 <= y < rows):
                continue
            
            if visited[y][x]:
                continue

            visited[y][x] = true

            for pointsToX, pointsToY in grid[y][x]:
                if 0 <= pointsToX < cols and 0 <= pointsToY < rows:
                    stack.append((pointsToX, pointsToY))

        return visited

    #depth first search
    valu = dfs(pipeGrid, startingPoint[0], startingPoint[1])

    sinksThatConnect = ""

    for letter in letterArr:
        if(letter.isalpha()):
            sinksThatConnect += letter

    return valu


print(solution("./input.txt"))
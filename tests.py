def test1():
    def tt():
        return ((1,2),(2,1))

    gg = tt()

    point = (1,2)

    for hh in gg:
        print(hh)
        if(point == hh):
            print("oh wowie")

def test2():
    yy = {(1,2),(2,3),(0,3),(3,0)}

    p = {(3,0)}

    print(p.issubset(yy))
    print(yy.issubset(p))
    print(p.issuperset(yy))
    print(yy.issuperset(p))
    print(type(yy))
    print(p)

def test3():
    listuno = [1,2,3,3,4,5]
    listdos = listuno.copy()
    listdos.clear()
    print(listuno)
    print(listdos)

def test4():
    class ooo:
        def __init__(self, one, two):
            self.x = one
            self.y = two
        def ts(self):
            return str((self.x, self.y))

    ooolist = []
    
    def printList(list):
        for item in list:
            print(item)

    for i in range(2):
        for j in range(2):
            ooolist.append(ooo(i, j))

    

test2()

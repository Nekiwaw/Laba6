def glubina():
    derevo = {
        1 : [2,3],
        2 : [4,5],
        3 :[6,7],
        4 : [8,9],
        5 : [],
        6 : [],
        7 : [],
        8 : [],
        9 : []
    }

    posesh = set()

    def dfs(j):
        if j in posesh:
            return
        posesh.add(j)
        for i in derevo[j]:
            if not i in posesh:
                dfs(i)
    s=1
    dfs(s)
    print(posesh)
def shirina():
    derevo = {
        1 : [9,8],
        9 : [7,6],
        8 :[5,4],
        7 : [3,2],
        6 : [],
        5 : [],
        4 : [],
        3 : [],
        2 : []
    }

    posesh = set()
    ocher = []
    BFS = []


    def bfs(j):
        if j in posesh:
            return
        posesh.add(j)
        BFS.append(j)
        for i in derevo[j]:
            if not i in posesh:
                ocher.append(i)
        while ocher:
            bfs(ocher.pop(0))

    s = 1
    bfs(s)
    print(BFS)
glubina()
shirina()

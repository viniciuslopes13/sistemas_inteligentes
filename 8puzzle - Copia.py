import copy

class State:
    def __init__(self,n,parent):
        self.n = n
        self.parent = parent

def initialState():
    state = [[1,2,3],[4,0,5],[7,8,6]]
    return State(state,None)

def showState(s):
    print("==========")
    for row in s.n:
        print(row)
    print("==========")

def findZero(s):
    l=0
    for row in s.n:
        c=0
        for column in row:
            if(column==0):
                return (l,c)
            c=c+1
        l=l+1
    return (0,0)

def moveUp(s,l,c):
    s.n[l][c] = s.n[l-1][c]
    s.n[l-1][c] = 0

def moveDown(s,l,c):
    s.n[l][c] = s.n[l+1][c]
    s.n[l+1][c] = 0

def moveLeft(s,l,c):
    s.n[l][c] = s.n[l][c-1]
    s.n[l][c-1] = 0

def moveRight(s,l,c):
    s.n[l][c] = s.n[l][c+1]
    s.n[l][c+1] = 0

def copyState(s):
    s2 = copy.deepcopy(s)
    return s2

def isGoal(s):
    goalState=[[1,2,3],[4,5,6],[7,8,0]]
    l=0
    for row in goalState:
        c=0
        for e in row:
            if(s.n[l][c]!=goalState[l][c]):
                return False
            c=c+1
        l=l+1
    return True

def expand(s):
    children = []

    (l,c) = findZero(s)

    if (l>0):
        state_ = State(copyState(s).n,s)
        moveUp(state_,l,c)
        children.append(state_)
    if(l<2):
        state_ = State(copyState(s).n,s)
        moveDown(state_,l,c)
        children.append(state_)
    if(c>0):
        state_ = State(copyState(s).n,s)
        moveLeft(state_,l,c)
        children.append(state_)
    if(c<2):
        state_ = State(copyState(s).n,s)
        moveRight(state_,l,c)
        children.append(state_)

    return children
    
def filaVazia():
    return len(fila)==0

def enfileira(s):
    fila.append(s)

def desenfileira():
    ret = fila[0]
    del fila[0]
    return ret 

def mostrarCaminho(s):
    if s is None:
        return
    mostrarCaminho(s.parent)
    showState(s)


state=initialState()
fila = []
enfileira(state)
while not filaVazia():
    estadoAtual = desenfileira()
    if isGoal(estadoAtual):
        print("Estado objetivo encontrado!")
        mostrarCaminho(estadoAtual)
        break
    showState(estadoAtual)
    estadosFilhos = expand(estadoAtual)
    for filho in estadosFilhos:
        enfileira(filho)


#if(isGoal(state)):
#    print("Estado objetivo")

#if(not isGoal(state)):
#    print("Nao estado objetivo")
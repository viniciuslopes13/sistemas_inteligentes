state = [[1,2,3],[4,0,5],[7,8,6]]

class State:
    def __init__(self,n,parent):
        self.n = n
        self.parent = parent

def initialState():
    return State(state,None)

def showState(state):
    print("==========")
    for row in state:
        print(row)
    print("==========")

def findZero(state):
    l=0
    for row in state:
        c=0
        for column in row:
            if(column==0):
                return (l,c)
            c=c+1
        l=l+1
    return (0,0)

def moveUp(state,l,c):
    state[l][c] = state[l-1][c]
    state[l-1][c] = 0

def moveDown(state,l,c):
    state[l][c] = state[l+1][c]
    state[l+1][c] = 0

def moveLeft(state,l,c):
    state[l][c] = state[l][c-1]
    state[l][c-1] = 0

def moveRight(state,l,c):
    state[l][c] = state[l][c+1]
    state[l][c+1] = 0

def copyState(state):
    ret=[]
    for row in state:
        row_ = []
        for e in row:
            row_.append(e)
        ret.append(row_)
    return ret

def isGoal(state):
    goalState=[[1,2,3],[4,5,6],[7,8,0]]
    l=0
    for row in goalState:
        c=0
        for e in row:
            if(state[l][c]!=goalState[l][c]):
                return False
            c=c+1
        l=l+1
    return True

def expand(state):
    children = []

    (l,c) = findZero(state)

    if (l>0):
        state_ = copyState(state)
        moveUp(state_,l,c)
        children.append(state_)
    if(l<2):
        state_ = copyState(state)
        moveDown(state_,l,c)
        children.append(state_)
    if(c>0):
        state_ = copyState(state)
        moveLeft(state_,l,c)
        children.append(state_)
    if(c<2):
        state_ = copyState(state)
        moveRight(state_,l,c)
        children.append(state_)

    return children
    
def filaVazia():
    return len(fila)==0

def enfileira(state):
    fila.append(state)

def desenfileira():
    ret = fila[0]
    del fila[0]
    return ret 

def mostrarCaminho(s):
    if s is None:
        return
    mostrarCaminho(s[4])
    showState(s)

fila = []
enfileira(state)
while not filaVazia():
    estadoAtual = desenfileira()
    if isGoal(estadoAtual):
        print("Estado objetivo encontrado!")
        showState(estadoAtual)
        break
    showState(estadoAtual)
    estadosFilhos = expand(estadoAtual)
    for filho in estadosFilhos:
        enfileira(filho)


#if(isGoal(state)):
#    print("Estado objetivo")

#if(not isGoal(state)):
#    print("Nao estado objetivo")
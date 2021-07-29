class State:
    def __init__(self,n, depth):
        self.n = n
        self.depth = depth

def initialState():
    return State(1,0)

def stackIsEmpty():
    return len(stack) == 0

def showState(s):
    print(s.n)

def expand(s):
    if s.n >= 4:
        return []
    ret = []
    
    ret.append(State(2*s.n + 1,s.depth+1))
    ret.append(State(2*s.n, s.depth+1))
    return ret

stack = []

def push(s):
    stack.append(s)

def pop():
    return stack.pop()

depthLimit = 0

while True:
    s = initialState()
    push(s)
    currentMax = 0
    while not stackIsEmpty():
        current = pop()
        showState(current)
        children = expand(current)
        for child in children:
            if(current.depth<depthLimit):
                push(child)
            if(current.depth>currentMax):
                currentMax=current.depth
    
    if (currentMax<depthLimit):
        break
    
    depthLimit=depthLimit+1
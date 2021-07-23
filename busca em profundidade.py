class State:
    def __init__(self,n):
        self.n = n

def initialState():
    return State(1)

def stackIsEmpty():
    return len(stack) == 0

def showState(s):
    print(s.n)

def expand(s):
    if s.n >= 4:
        return []
    ret = []
    
    ret.append(State(2*s.n + 1))
    ret.append(State(2*s.n))
    return ret

stack = []

def push(s):
    stack.append(s)

def pop():
    return stack.pop()


s = initialState()

push(s)

while not stackIsEmpty():
    current = pop()
    showState(current)
    children = expand(current)
    for child in children:
        push(child)

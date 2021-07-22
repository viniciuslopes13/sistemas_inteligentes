class State:
    def __init__(self,n):
        self.n = n

def initialState():
    return State(1)

def queueIsEmpty():
    return len(queue) == 0

def showState(s):
    print(s.n)

def expand(s):
    if s.n >= 4:
        return []
    ret = []
    ret.append(State(2*s.n))
    ret.append(State(2*s.n + 1))
    return ret

queue = []

def enqueue(s):
    queue.append(s)

def dequeue():
    ret = queue[0]
    del queue[0]
    return ret


s = initialState()

enqueue(s)

while not queueIsEmpty():
    current = dequeue()
    showState(current)
    children = expand(current)
    for child in children:
        enqueue(child)

class State:
    def __init__(self,n, parent):
        self.n = n
        self.parent = parent

def initialState():
    return State(1, None)

def queueIsEmpty():
    return len(queue) == 0

def showState(s):
    print(s.n)

def expand(s):
    if s.n >= 4:
        return []
    ret = []
    ret.append(State(1,s))
    ret.append(State(2,s))
    ret.append(State(3,s))
    ret.append(State(2*s.n, s))
    ret.append(State(2*s.n + 1, s))
    return ret

queue = []

def enqueue(s):
    queue.append(s)

def dequeue():
    ret = queue[0]
    del queue[0]
    return ret

def isGoal(s):
    return s.n==7

def showPath(s):
    if s is None:
        return
    showPath(s.parent)
    showState(s)

def isEqual(s1,s2):
    return s1.n == s2.n

def isOnPath(child, ancestor):
    if ancestor is None:
        return False
    if isEqual(child,ancestor):
        return True
    return isOnPath(child,ancestor.parent)

def isOpenState(s):
    for state in queue:
        if isEqual(s,state):
            return True
    return False

def isOnExpandedStates(s):
    for state in expandedStates:
        if isEqual(s,state):
            return True
    return False

expandedStates = []

s = initialState()

enqueue(s)

while not queueIsEmpty():
    current = dequeue()
    if isOnExpandedStates(current):
        continue
    if isGoal(current):
        print('Reached goal!')
        showPath(current)
        break
    showState(current)
    children = expand(current)
    expandedStates.append(current)
    for child in children:
        if (not isOnPath(child, current)) and (not isOpenState(child)):
            enqueue(child)

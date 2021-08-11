state = [[1,2,3],[4,0,5],[7,8,6]]

class State:
    def __init__(self,n,parent):
        self.n = n
        self.parent = parent

def initialState():
    return State(state,None)

def showState(s):
    print("==========")
    for row in s.n:
        print(row)
    print("==========")

EstadoInicio = initialState()
showState(EstadoInicio)


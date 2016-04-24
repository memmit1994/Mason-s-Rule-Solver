
def getPaths(start,end,edges,visited=[],paths=[]):
    if len(visited) ==0: visited.append(start)
    for neighbour in edges[visited[0]]:
        if neighbour not in visited:
            visited.insert(0,neighbour)
            if neighbour == end: paths.append(list(reversed(visited)))
            getPaths(start,end,edges,visited,paths)
    visited.pop(0)

def getCycleFromNode(start,edges,visited=[],paths=[]):
    if len(visited) ==0: visited.append(start)
    for neighbour in edges[visited[0]]:
        if neighbour == start:
            paths.append(list(reversed([neighbour]+list(visited))))
        if neighbour not in visited:
            visited.insert(0,neighbour)
            if neighbour == start:
                paths.append(list(visited))
            getCycleFromNode(start,edges,visited,paths)
    visited.pop(0)

def getCycles(edges):
    cycles = []
    for v in edges.keys():
        vCycles = []
        getCycleFromNode(v,edges,[],vCycles)
        for cycle in vCycles:
            if not repeatedCycle(cycle,cycles):
                cycles.append(cycle)
    return cycles

def repeatedCycle(c,cycles):
    for cycle in cycles:
        if cyclesEqual(cycle,c):
            return True
    return False
def cyclesEqual(c1,c2):
    if len(c1) != len(c2): return False

    cd1=getDistinct(c1)
    cd2 = getDistinct(c2)

    for i in range(len(cd1)):
        if cd1[i]!=cd2[i]:
            return False
    return True

def getDistinct(c):
    result=set()
    for x in c:
        result.add(x)
    return list(result)

def getDelta(loops,gains):
    delta = "1 "
    for index in loops.keys():
        if len(loops[index])!=0:
            coeff = "+ (" if (-1)**index >0 else "- ("
            delta+=str(coeff)
        for x in loops[index]:
            delta+=getCycleGain(x,gains)
            if x is not loops[index][-1]:
                delta+=" + "

        delta+=") " if index!=loops.keys()[-1] else ""
    return delta

def getPathGain(path,gains):
    result=""
    #if len(path) >1
    result+=gains[path[0],path[1]]
    for i in range(1,len(path)-1):
        result+=" * "+gains[path[i],path[i+1]]
    return result


def getDeltaOfPath(cycles,path,gains):
    resultCycles=list(cycles)
    resultDelta=""
    for cycle in cycles:
        if loopsTouching(cycle,path):
            resultCycles.remove(cycle)
    for c in resultCycles:
        resultDelta+=getCycleGain(c,gains)
        if c != resultCycles[-1]:
            resultDelta+=" + "
    resultDelta = "1 - 0" if len(resultCycles)==0 else "1 - ("+resultDelta+")"

    return resultDelta


def getNumerator(cycles,paths,gains):
    result =""
    for path in paths:
        result+="("+getPathGain(path,gains)+")"+" * ("+getDeltaOfPath(cycles,path,gains)+")"
        result+=" + "  if path != paths[-1] else ""
    return result
def getCycleGain(cycle,gains):
    result=""
    i=0
    n=len(cycle)-1
    startOfCycle = cycle[0]
    while i <n:
        if((cycle[i],cycle[i+1])) in gains:
            result+= " *" if i!=0 else ""
            result+=gains[(cycle[i],cycle[i+1])]
            if cycle[i + 1] == startOfCycle and len(cycle) >2:
                startOfCycle = cycle[i+2] if i+2 <n else startOfCycle
                i+=2
                continue
        i+=1
    return result

def loopsTouching(c1,c2):
    for x in c1:
        if x in c2:
            return True
    return False


def getNonTouching(cycles,i=1,loops={}):
    if len(loops)==0 : loops[1]=cycles
    i+=1
    loops[i]=[]
    for j in range(len(loops[i - 1])):
        for cycle in cycles:
            if not loopsTouching(loops[i-1][j],cycle):
                 if not listExistsIn((loops[i-1][j]+cycle),loops[i]):
                    loops[i].append(loops[i-1][j]+cycle)
    if len(loops[i])!=0:
        getNonTouching(cycles,i,loops)

def listsEqual(l1,l2):
    if len(l1)!=len(l2): return False
    for x in l1:
        if x not in l2:
            return False
    return True

def listExistsIn(list,listOfLists):
    for x in listOfLists:
        if listsEqual(list,x):
            return True
    return False

def removeEmptyStrings(list):
    if list is not None:
        for x in list:
            if x == "":
                list.remove(x)
    return list
def StringListToNums(list):
    if list is not None:
        for i in range(len(list)):
            list[i]=int(list[i])
    return list

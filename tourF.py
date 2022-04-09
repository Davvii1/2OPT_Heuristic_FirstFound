
def getEdges(T):
    edges = []
    # Get edges
    # T example : T = [1, 4, 3, 6, 2, 7, 8, 5]
    for x in range(len(T)):
        if x == len(T) - 1:
            edge = str(T[x]) + "-" + str(T[0])
        else:
            edge = str(T[x]) + "-" + str(T[x + 1])
        edges.append(edge)
    # print("Edges:", edges)
    return edges


def getNextTour(edges, EdgePoints):
    # Get points to be replaced
    # EdgePoints example : EdgePoints = [[4, 3], [6, 2]]
    prevP = EdgePoints
    prevPidx = edges.index(str(prevP[0][0]) + "-" + str(prevP[0][1])), \
               edges.index(str(prevP[1][0]) + "-" + str(prevP[1][1]))

    # New Points
    newP = [[prevP[0][0], prevP[1][0]], [prevP[0][1], prevP[1][1]]]
    newPlist = []
    [newPlist.append(str(y[0]) + "-" + str(y[1])) for y in newP]

    # Eliminate Points
    eR = []
    [eR.append(x) for x in edges]
    [eR.remove(str(y[0]) + "-" + str(y[1])) for y in prevP]
    # print("Not removed edges:", eR)

    # Get reversible edges
    sP1 = edges[prevPidx[0] + 1:prevPidx[1]]
    sP2 = [x for x in eR if x not in sP1]
    # print("Subpath 1: ", sP1)
    # print("Subpath 2: ", sP2)
    rsp1 = []
    if len(sP1) <= len(sP2):
        rP = sP1
    else:
        rP = sP2
    for x in rP:
        rsp = x.split("-")
        rsp1.append(rsp[1] + "-" + rsp[0])
    # print("Reverse subpath:", rsp1)

    # Form New Tour
    ntr = []
    nT = []
    [ntr.append(x) for x in edges]
    ntr[prevPidx[0]] = newPlist[0]
    ntr[prevPidx[1]] = newPlist[1]
    Rind = [ntr.index(x) for x in rP]
    for x in range(len(rsp1)):
        ntr[Rind[x]] = rsp1[x]
    nT.append(ntr[0])
    for x in nT:
        lastn = x.split("-")[1]
        nextE = [(x.split("-")[0], x.split("-")[1]) for x in ntr if lastn in x and x not in nT]
        try:
            if nextE[0][0] == lastn:
                nT.append(str(nextE[0][0]) + "-" + str(nextE[0][1]))
            else:
                nT.append(str(nextE[0][1]) + "-" + str(nextE[0][0]))
        except:
            pass
    # print("New Edges:", nT)
    ptpT = []
    [ptpT.append(x.split("-")[0]) and ptpT.append(x.split("-")[1]) for x in nT if x not in ptpT]
    sinx = ptpT.index(str(1))
    for x in range(sinx):
        if ptpT[x] not in ptpT:
            ptpT.append(ptpT[x])
        ptpT.remove(ptpT[x])
    # print("New Tour:", ptpT)
    return nT, list(map(int, ptpT))

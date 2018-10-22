import pandas
import random

def nDiffs(w1, w2):
    nDs = 0
    for i in range(len(w1)):
        if (w1[i] != w2[i]):
            nDs += 1
    return (nDs)

def printPathToRoot(w):
    print(w)
    if (targets[w] == None):
        return(w)
    else:
        return(printPathToRoot(targets[w]))


def findRoot(w):
    if(targets[w] == None):
        return(w)
    else:
        return(findRoot(targets[w]))


words = open("C:\\Users\\Jamie\\PycharmProjects\\WordPathFinder\\dictionary.txt").readlines()
for i in range(len(words)):
    words[i] = words[i].strip()

wordsByN = [set() for i in range(50)]

for w in words:
    n = len(w)
    wordsByN[n].add(w)

for i in range(50):
    print(str(i) + "  " + str(len(wordsByN[i])))

wordList = list(wordsByN[4])

targets = {}
for w in wordList:
    targets[w] = None

nLinks = 0
for i in range(len(wordList)):
    for j in range(i + 1, len(wordList), 1):

        wI = wordList[i]
        wJ = wordList[j]

        rootI = findRoot(wI)
        if(rootI != wI):
            targets[wI] = rootI
        rootJ = findRoot(wJ)
        if(rootJ != wJ):
            targets[wJ] = rootJ

        #if wI and wJ should be in the same group
        if(nDiffs(wI, wJ) == 1):
            nLinks += 1
            #if they're not already
            if(findRoot(wI) != findRoot(wJ)):
                targets[findRoot(wJ)] = findRoot(wI)


print("condensing tree")
for i in range(10):
    for w in wordList:
        if(findRoot(w) != w):
            targets[w] = findRoot(w)

rootList = set([findRoot(w) for w in wordList])
for l in set(targets.values()):
    if(l not in rootList):
        print(l)

print(nLinks)

groups = pandas.Series(list(targets.values()))

print(groups.value_counts())

labels = list(set([findRoot(w) for w in wordList]))
wordGroups = {}
for l in labels:
    wordGroups[l] = []

for w in wordList:
    wordGroups[findRoot(w)].append(w)

def groupSize(l):
    return(-1*len(wordGroups[l]))

labels = sorted(labels, key=groupSize)

outfile = open("groups4.txt", 'w')

for l in labels:
    gL = sorted(wordGroups[l])
    print(str(len(gL)) + ' - ' + str(gL))
    outfile.write(str(len(gL)) + ' - ' + str(gL))
import numpy as np

def firstValGreater(arr, val):
    for index, x in np.ndenumerate(arr):
        if x >= val:
            return index[0] + 1
    return len(arr)

def stringToForest(list_of_strings):
    dim = len(list_of_strings)
    forest = np.zeros(shape=(dim, dim), dtype=int)
    for indexrow in np.arange(dim):
        for indexcolumn in np.arange(dim):
            forest[indexrow, indexcolumn]=list_of_strings[indexrow][indexcolumn]
    return forest

def numTreesVisible(forest):
    visibleCounter = 0
    for indexrow in range(forest.shape[0]):
        for indexcolumn in range(forest.shape[1]):
            if indexrow == 0 or indexrow == forest.shape[0]-1 or indexcolumn == 0 or indexcolumn == forest.shape[1]-1:
                visibleCounter += 1
            else:
                treeHeight = forest[indexrow, indexcolumn]
                if treeHeight > np.max(forest[:indexrow, indexcolumn]) or treeHeight > np.max(forest[indexrow+1:, indexcolumn]) or treeHeight > np.max(forest[indexrow, :indexcolumn]) or treeHeight > np.max(forest[indexrow, indexcolumn+1:]):
                    visibleCounter += 1

    return visibleCounter

def maxVisScore(forest):
    visScore = np.zeros_like(forest)

    for index, x in np.ndenumerate(forest):
        visDistList = []
        visDistList.append(firstValGreater(forest[index[0], index[1]+1:].reshape(-1), x))
        visDistList.append(firstValGreater(np.flip(forest[index[0], :index[1]]).reshape(-1), x))
        visDistList.append(firstValGreater(forest[index[0]+1:, index[1]].reshape(-1), x))
        visDistList.append(firstValGreater(np.flip(forest[:index[0], index[1]]).reshape(-1), x))
        visScore[index] = visDistList[0]*visDistList[1]*visDistList[2]*visDistList[3]


    return np.max(visScore)

list_of_strings = open('day8input.txt').readlines()
forest = stringToForest(list_of_strings)
print(numTreesVisible(forest))
print(maxVisScore(forest))

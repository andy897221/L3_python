import numpy as np

class Helper:
    def dual_to_mono(brs):
        monoBR = []
        for br in brs:
            if br[1] < br[0]: monoBR.append([br[1], br[0]])
            else: monoBR.append([br[0], br[1]])
        monoBR = Helper.pathStrs_to_list(set(Helper.list_to_pathStrs(monoBR)))
        return monoBR

    def filter_self_cycle(brs):
        noCycleBR = []
        for br in brs:
            if br[0] == br[1]: continue
            noCycleBR.append([br[0], br[1]])
        return noCycleBR

    def to_dual_binary_relation(binary_relation):
        binary_relation_plus = binary_relation.copy()
        for i in binary_relation:
            binary_relation_plus.append([i[1], i[0]])
        binary_relation_plus = Helper.list_to_pathStrs(binary_relation_plus)
        binary_relation_plus = list(set(binary_relation_plus))
        binary_relation_plus = Helper.pathStrs_to_list(binary_relation_plus)
        return binary_relation_plus
    
    def pathStr(path):
        # given a list, serialize the list of elements as str, return a str
        return "\t".join([str(i) for i in path])

    def list_to_pathStrs(paths):
        return [Helper.pathStr(path) for path in paths]

    def pathStrs_to_list(pathStr, isInt=False):
        # given a list of str (the str is a serialized list), de-serialize them, return a list of lists
        if isInt:
            paths = [i.split("\t") for i in pathStr]
            intPaths = []
            for path in paths:
                intPaths.append([])
                for i in path: intPaths[-1].append(int(i))
            return intPaths
        else:
            return [i.split("\t") for i in pathStr]

    def binary_to_relation(binaryRelat, rSet=False):
        nodes = Helper.binary_relation_to_node(binaryRelat)
        # build dict
        relation = {}
        if rSet:
            for node in nodes: relation[node] = set()
            for nodeArr in binaryRelat: relation[nodeArr[0]].add(nodeArr[1])
        else:
            for node in nodes: relation[node] = []
            for nodeArr in binaryRelat: relation[nodeArr[0]].append(nodeArr[1])
        return relation

    def binary_relation_to_node(binary_relation):
        return set(list(np.unique(np.asarray(binary_relation).flatten())))
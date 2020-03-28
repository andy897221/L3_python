import traversalHelper as tr
from itertools import combinations
import helper as hr
import math
import json, sys, os

class ns:
    BRToRelat = tr.Helper.binary_to_relation
    toDualBR = tr.Helper.to_dual_binary_relation
    BRToNode = tr.Helper.binary_relation_to_node
    arr_pStr = tr.Helper.list_to_pathStrs
    pStr_arr = tr.Helper.pathStrs_to_list
    br_str = tr.Helper.br_to_pathStr

def L3_normalization(PPIr, nodeX, nodeY):
    uvPair, candidateUs, candidateVs = get_uv(nodeX, nodeY, PPIr)
    score = 0
    for uv in uvPair:
        if math.sqrt(len(PPIr[uv[0]])*len(PPIr[uv[1]])) == 0: continue
        score += 1/math.sqrt(len(PPIr[uv[0]])*len(PPIr[uv[1]]))
    return score

def get_uv(x, y, PPIr):
    candidateUs = PPIr[x]
    candidateVs = PPIr[y]
    uvPair = []
    for u in candidateUs:
        for v in candidateVs:
            if u not in PPIr[v]: continue
            uvPair.append([u,v])
    return uvPair, candidateUs, candidateVs

def PPILinkPred(samplePPIbr):
    samplePPIr = ns.BRToRelat(ns.toDualBR(samplePPIbr), rSet=True)
    sampleNodes = ns.BRToNode(samplePPIbr)
    nodePairs = list(combinations(sampleNodes, 2))
    scores, predictedPPIbrs = [], []
    for nodePair in nodePairs:
        [nodeX, nodeY] = nodePair
        if nodeY in samplePPIr[nodeX]: continue
        score = L3_normalization(samplePPIr, nodeX, nodeY)
        scores.append(score)
        predictedPPIbrs.append(nodePair)
    sortedPPIbrs, sortedScores = hr.sort_key_val(predictedPPIbrs, scores)
    return sortedPPIbrs, sortedScores
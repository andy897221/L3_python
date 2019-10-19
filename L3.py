import traversalHelper as tr
from itertools import combinations
import json, math
import bioGRID as bg
import helper as hr

toDualBR = tr.Helper.to_dual_binary_relation
toMonoBR = tr.Helper.dual_to_mono
arr_pStr = tr.Helper.list_to_pathStrs
pStr_arr = tr.Helper.pathStrs_to_list

def L3_normalization(PPIr, uvPair):
    score = 0
    for uv in uvPair:
        score += 1/math.sqrt(len(PPIr[uv[0]])*len(PPIr[uv[1]]))
        # score += 1/len(PPIr[uv[0]])*len(PPIr[uv[1]]) # worse result
    return score

def basic_L3(topNo, sampleFile="./data/custom/PPIsample_10percent.json"):
    # not exact implementation but close
    samplePPIbr = []
    with open(sampleFile, "r") as f: samplePPIbr = json.loads(f.read())
    PPIr = tr.Helper.binary_to_relation(toDualBR(samplePPIbr), rSet=True)
    nodes = tr.Helper.binary_relation_to_node(samplePPIbr)
    combs = list(combinations(nodes, 2))
    scores = []
    predictedPPIbrs = []
    for nodes in combs:
        if nodes[0] in PPIr[nodes[1]]: continue
        x, y = nodes[0], nodes[1]
        candidateUs = PPIr[x]
        candidateVs = PPIr[y]
        candidateUs = candidateUs-candidateVs
        candidateVs = candidateVs-candidateUs
        uvPair = []
        for u in candidateUs:
            for v in candidateVs:
                if u not in PPIr[v]: continue
                uvPair.append([u,v])
        score = L3_normalization(PPIr, uvPair)
        scores.append(score)
        predictedPPIbrs.append(nodes)

    scoresMap = {}
    for i in range(0, len(scores)): scoresMap[i] = scores[i]
    sortedMap = hr.key_sorted_by_val(scoresMap)
    sortedPPIbrs = [predictedPPIbrs[i] for i in sortedMap]
    predictedPPIbrs = sortedPPIbrs[0:topNo]

    PPIbr, _, _, _ = bg.parse_bioGRID()
    unaccountedBR = set(arr_pStr(PPIbr))-set(arr_pStr(toDualBR(samplePPIbr)))
    prec = len(set(arr_pStr(toDualBR(predictedPPIbrs)))&unaccountedBR)/len(toMonoBR(predictedPPIbrs))
    print("basic L3 prec: "+str(prec))
    return

if __name__ == "__main__":
    basic_L3(topNo=1000)
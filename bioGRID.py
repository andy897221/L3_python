import helper as hr
import numpy as np
from collections import defaultdict
import os, json
import traversalHelper as tr

def parse_bioGRID(filename="./data/BIOGRID_yeast_PPI.txt"):
    '''
    return PPIbr, PPIscores, GGIbr, GGIscores (data type: list)
    '''
    if os.path.exists("./data/parsed_yeast_PPI.json") and os.path.exists("./data/parsed_yeast_GGI.json"):
        PPIdata = {}
        with open("./data/parsed_yeast_PPI.json", "r") as f:
            PPIdata = json.loads(f.read())
        GGIdata = {}
        with open("./data/parsed_yeast_GGI.json", "r") as f:
            GGIdata = json.loads(f.read())
        return PPIdata["br"], [], GGIdata["br"], []

    data = defaultdict(list)
    with open(filename, "r") as f:
        head = f.readline().split("\t")
        # want to get, Official Symbol Interactor A, Official Symbol Interactor B, Experimental System Type, Score
        fields = ["Official Symbol Interactor A", "Official Symbol Interactor B", "Experimental System Type", "Score"]
        fieldsI = [hr.get_item_I(head, i) for i in fields]
        count = 0
        for line in f.readlines():
            row = line.split("\t")
            for field in range(0, len(fieldsI)): data[fields[field]].append(row[fieldsI[field]])

    # to gene-gene (genetic) interaction & protein-protein interaction
    GGInodeA, GGInodeB = [], []
    PPInodeA, PPInodeB = [], []
    GGIscores, PPIscores = [], []
    for i in range(0, len(data["Official Symbol Interactor A"])):
        if data["Experimental System Type"][i] == "genetic":
            GGInodeA.append(data["Official Symbol Interactor A"][i])
        else:
            PPInodeA.append(data["Official Symbol Interactor A"][i])
    for i in range(0, len(data["Official Symbol Interactor B"])):
        if data["Experimental System Type"][i] == "genetic":
            GGInodeB.append(data["Official Symbol Interactor B"][i])
        else:
            PPInodeB.append(data["Official Symbol Interactor B"][i])
    for i in range(0, len(data["Score"])):
        if data["Experimental System Type"][i] == "genetic":
            GGIscores.append(data["Score"][i])
        else:
            PPIscores.append(data["Score"][i])
    # to br
    GGIbr, PPIbr = [], []
    for i in range(0, len(GGInodeA)): GGIbr.append([GGInodeA[i], GGInodeB[i]])
    for i in range(0, len(PPInodeA)): PPIbr.append([PPInodeA[i], PPInodeB[i]])

    PPIbr = tr.Helper.dual_to_mono(PPIbr)
    GGIbr = tr.Helper.dual_to_mono(GGIbr)
    PPIbr = tr.Helper.filter_self_cycle(PPIbr)
    GGIbr = tr.Helper.filter_self_cycle(GGIbr)

    with open("./data/parsed_yeast_GGI.json", "w") as f:
        # f.write(json.dumps({"br": GGIbr, "scores": GGIscores}))
        f.write(json.dumps({"br": GGIbr}))
    with open("./data/parsed_yeast_PPI.json", "w") as f:
        f.write(json.dumps({"br": PPIbr}))
        # f.write(json.dumps({"br": PPIbr, "scores": PPIscores}))
    return PPIbr, [], GGIbr, []

if __name__ == "__main__":
    PPIbr, _, GGIbr, _ = parse_bioGRID()
    # print(len(PPIbr), len(GGIbr))
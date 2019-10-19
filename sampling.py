import bioGRID as bg
import random as rn
import json

def gen_PPIsample(percent, filename="./data/custom/PPIsample_50percent.json"):
    PPIbr, _, _, _ = bg.parse_bioGRID()
    partialPPIbr = rn.sample(PPIbr, int(len(PPIbr)*percent))
    with open(filename, "w") as f: f.write(json.dumps(partialPPIbr))
    return

if __name__ == "__main__":
    gen_PPIsample(0.1, filename="./data/custom/PPIsample_10percent.json")
    gen_PPIsample(0.3, filename="./data/custom/PPIsample_30percent.json")
    gen_PPIsample(0.5, filename="./data/custom/PPIsample_50percent.json")
    gen_PPIsample(0.7, filename="./data/custom/PPIsample_70percent.json")
    gen_PPIsample(0.9, filename="./data/custom/PPIsample_90percent.json")
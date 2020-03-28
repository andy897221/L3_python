import ppiLPred

# assume a PPI dataset 
# each list within this list is a PPI, where each item is a protein
ppi = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['A', 'E'], ['E', 'F'], ['F', 'D']]
sortedPPI, sortedScores = ppiLPred.PPILinkPred(ppi)
print(sortedPPI, sortedScores) # [('C', 'E'), ('D', 'A'), ('B', 'F'), ('C', 'A'), ('C', 'F'), ('D', 'B'), ('D', 'E'), ('A', 'F'), ('B', 'E')] [1.0, 1.0, 1.0, 0, 0, 0, 0, 0, 0]
# according to L3, proteins that are 3-hops away will likely have PPI
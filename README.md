# L3_python
Third-party implementation in Python of L3 algorithm in "Network-based prediction of protein interactions" on Nature Communication 2019, doi: https://doi.org/10.1038/s41467-019-09177-y, its GitHub (implemented in C++): kpisti/L3

# Description
The `ppiLPred.py` implemented the main L3 algorithm, and the `example.py` provided an example of using the algorithm. A minimum sample of PPI dataset is defined in the `example.py`.

# Pseudocode
Let `n(x)` returns a set of neighbor nodes of `x`, `candidatePPIs` as a set of non-existing undirected edges of the PPI dataset, with the data structure `[[A, B], ..., [Y,Z]]` where `[A, B]` is a candidate PPI.

```python
def L3(candidatePPIs):
    PPIScores = {}
    for [X, Y] in candidatePPIs:
        U = n(X), V = n(Y)
        uvPair = [all possible combinations for nodes between U and V]
        score = 0
        for [u, v] in uvPair:
            score += 1/sqrt(|n(u)|*|n(v)|)
        PPIScores[[X, Y]] = score
    return sort(PPIScores)
```
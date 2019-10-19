# L3_python
Python implementation of L3 algorithm in "Network-based prediction of protein interactions" on Nature Communication, doi: https://doi.org/10.1038/s41467-019-09177-y, its GitHub (implemented in C++): kpisti/L3

# Requirement
```pip install numpy```

# File Structure
```bioGRID.py```: parsing the downloaded BioGRID file into a data structure of PPI binary relation e.g. ```[[a,b],[c,d]]``` means an undirected graph of node {a,b,c,d} where a & b are connected, c & d are connected

```sampling.py```: randomly delete a certain ratio of BioGRID edges for data pre-processing of L3 algorithm benchmark

```helper.py```,```traversalHelper.py```: some helper function

```L3.py```: the re-implementation of L3 algorithm in Python

# Usage
run ```L3.py``` (see line 57 ```basic_L3()``` as an example). By default it uses a file of "sampled 90% edges in BioGRID PPI", and returns the top 1000 predicted edges by L3. The program then prints the precision of the prediction i.e. ratio of edges predicted correctly.

# Performance
Though not deterministic (for the same input, the prec returns differently everytime), performance varies from +/-0.05 of L3 performance (tested original L3 algorithm in C++ against the same dataset)

# Credits
To the paper, doi: https://doi.org/10.1038/s41467-019-09177-y

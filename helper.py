import numpy as np
from operator import itemgetter
import sys

def get_item_I(arr, item):
    # unique item
    return np.where(np.asarray(arr) == item)[0][0]

# source: https://www.geeksforgeeks.org/python-program-for-quicksort/
def partition(arr,start,end, refArr): 
    i = start-1
    pivot = arr[end]
    for j in range(start, end): 
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i]
            refArr[i], refArr[j] = refArr[j], refArr[i]
    arr[i+1],arr[end] = arr[end],arr[i+1] 
    refArr[i+1],refArr[end] = refArr[end],refArr[i+1] 
    return i+1
  
# Function to do Quick sort 
def referenceSort(arr,start,end, refArr): 
    if start < end: 
        pi = partition(arr,start,end, refArr)
        referenceSort(arr, start, pi-1, refArr) 
        referenceSort(arr, pi+1, end, refArr) 


def key_sorted_by_val(d, lowToHigh=False):
    if lowToHigh:
        sortedD = sorted(d.items(), key=itemgetter(1))
    else:
        sortedD = sorted(d.items(), key=itemgetter(1), reverse=True)
    sortedKey = [k for k, _ in sortedD]
    return sortedKey


if __name__ == "__main__":
    arr = [2,1,3]
    refArr = [1,2,3]
    referenceSort(arr, 0, 2, refArr)
    print(arr, refArr)
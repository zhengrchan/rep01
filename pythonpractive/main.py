from sort import Sort
from insert_sort import InsertSort
from merge_sort import MergeSort
from quick_sort import QuickSort

import numpy as np
import matplotlib.pyplot as plt

import random
import sys

rdmlist = np.random.randint(100, size=10)
asdlist = list(range(1, 901))
# print(rdmlist)

#isort = InsertSort(rdmlist)
#msort = MergeSort(rdmlist)
qsort = QuickSort(asdlist)

# isort.time(isort.insert_sort)
qsort.time(qsort.quick_sort)
print(qsort.run_time)

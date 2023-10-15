import pandas as pd
import numpy as np
from pprint import pprint


def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def k_nearest_neighbors(n, k):
    penguin = data[n]
    res = list(range(k))
    for i in range(k):
        nearest = 10 ** 100
        for j in range(len(data)):
            w = distance(list(penguin), list(data[j]))
            if j != n and (list(data[j]) not in res) and w < nearest:
                res[i] = list(data[j])
                nearest = w
    return np.array(res)


n = int(input())
k = int(input())
df = pd.read_csv('penguins.csv')
df.dropna(inplace=True)
data = np.array(df[['bill_length_mm', 'bill_depth_mm']])
result = k_nearest_neighbors(n, k)
pprint(*result, sep='\n')

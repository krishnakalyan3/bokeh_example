#!/usr/bin/env python3
import pandas as pd

kmeans_data = {'realease': ['tag1', 'tag2', 'tag3'], 'time': [1.5, 2, 2.1]}
df = pd.DataFrame(kmeans_data)
print(df)
import numpy as np
import sys

print(sys.version_info)

asList = [1, 2, 3]
asArray = np.array([1, 2, 3])  # 1D array
rowVec = np.array([[1, 2, 3]])  # row
colVec = np.array([[1], [2], [3]])  # column
'''
The Dimensions of Different Matrix 
'''
print(f'asList: {np.shape(asList)}')
print(f'asArray: {asArray.shape}')
print(f'rowVec: {rowVec.shape}')
print(f'colVec: {colVec.shape}')

print(sys.executable)

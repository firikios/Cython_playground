import numpy as np
import copy
from ExtensionTypes.node import CyList
from tqdm import tqdm
from pylist.pylist import List as PyList
import time

M = 10000000
D = 13
X = np.random.randn(M*D).reshape((M, D))
X = X.astype(dtype=np.dtype("f"))

cylist = CyList(D)
pylist = PyList()

for i, x in tqdm(enumerate(X)):
    cylist.addfront(x)

for i, x in tqdm(enumerate(X)):
    pylist.addfront(x)

idx = 4
query = copy.copy(X[idx,:])
print(f'X[{idx}]:{query}')
del X

start = time.time()
res_cy = cylist.findValue(query)
end = time.time()
cy_dt = end-start
print(f'cython findValue() ellapsed time :{cy_dt}')

start = time.time()
res_py = pylist.findValue(query)
end = time.time()
py_dt = end-start
print(f'python findValue() ellapsed time :{py_dt}')
print(f'rel_diff:{(cy_dt-py_dt)/py_dt*100}')

print(f'res_cy: {res_cy}')
print(f'res_py: {res_py}')
print('------------------------------------------')

start = time.time()
cylist.delitem(query)
end = time.time()
cy_dt  = end-start
print(f'cython delitem() ellapsed time :{cy_dt}')

start = time.time()
pylist.delitem(query)
end = time.time()
py_dt  = end-start
print(f'python delitem() ellapsed time :{py_dt}')
print(f'rel_diff:{(cy_dt-py_dt)/py_dt*100}')


from tqdm import tqdm
import itertools
import numpy as np
import matplotlib.pyplot as plt

n = int(input("N? ")) + 1
mod = int(input("Mod? "))
p = [[1],[0,1]]

for n in tqdm(range(2,n)):
    # Multiplies n-1 term by u #
    u = p[n-1].copy()
    u.insert(0,0)
    nextn = list(map(sum, itertools.zip_longest([i * 2 for i in u], [i * -1 for i in p[n-2]], fillvalue=0)))
    modn = [i % mod for i in nextn]
    p.append(modn)

plt.imshow(np.array(list(itertools.zip_longest(*p, fillvalue=0))).T, interpolation='none')
print('Complete')
plt.show()

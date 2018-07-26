import itertools
import numpy as np
from matplotlib import pyplot
from tqdm import tqdm

n = int(input("N? ")) - 1
p = [[1],[0,1]]

for n in tqdm(range(2,n)):
    # Multiplies n-1 term by u #
    u = p[n-1].copy()
    u.insert(0,0)
    nextn = list(map(sum, itertools.zip_longest([i * 2 for i in u], [i * -1 for i in p[n-2]], fillvalue=0)))
    p.append(nextn)

mod = p.copy()

print('')

modulus = int(input("Mod? "))

for n in tqdm(range(len(mod))):
    mod[n] = [i % modulus for i in mod[n]]

print("Complete")

print('\n'.join([''.join(['{:3}'.format(item) for item in row])
      for row in mod]))

pyplot.imshow(np.array(list(itertools.zip_longest(*mod, fillvalue=0))).T, interpolation='nearest')
pyplot.show()

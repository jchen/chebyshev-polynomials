import itertools

n = int(input("N? (Must be greater than 3) ")) - 1
p = [[1],[0,1]]

for n in range(2,n):
    # Multiplies n-1 term by u #
    u = p[n-1].copy()
    u.insert(0,0)

    # Multiplies u(n-1) term by 2 #
    a = [i * 2 for i in u]

    # Inverses n-2 term #
    b = [i * -1 for i in p[n-2]]
    #Debug:# print(a)
    #Debug:# print(b)
    add = list(map(sum, itertools.zip_longest(a, b, fillvalue=0)))
    #Debug:# print(add)
    p.append(add)

#print(p)

reversedp = p.copy()

#for n in range(len(reversedp)):
#    reversedp[n].reverse()

modp = reversedp.copy()

mod = int(input("Mod? "))

for n in range(len(modp)):
    modp[n] = [i % mod for i in modp[n]]

#print('\n'.join([''.join(['{:10}'.format(item) for item in row])
#      for row in reversedp]))

print('\n'.join([''.join(['{:3}'.format(item) for item in row])
      for row in modp]))

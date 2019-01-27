import itertools

# Prints the final polynomial #
def poly(self):
    # joiner[first, negative] = str
    joiner = {
        (True, True): '-',
        (True, False): '',
        (False, True): ' - ',
        (False, False): ' + '
    }

    result = []
    for power, coeff in reversed(list(enumerate(self))):
        j = joiner[not result, coeff < 0]
        coeff = abs(coeff)
        if coeff == 1 and power != 0:
            coeff = ''

        f = {0: '{}{}', 1: '{}{}x'}.get(power, '{}{}x^{}')

        result.append(f.format(j, coeff, power))

    return ''.join(result) or '0'


n = int(input("N? (Must be greater than 3) ")) + 1
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
    add = list(map(sum, itertools.zip_longest(a, b, fillvalue = 0)))
    #Debug:# print(add)
    p.append(add)

#Debug:# print(p)

print('')
for n in range(len(p)):
    print("T_" + str(n) + " = " + poly(p[n]))
    print('')

# Calculating the mods #
mod = int(input("Mod? "))
modp = p.copy()
for n in range(len(modp)):
    modp[n] = [i % mod for i in modp[n]]

print('')
for n in range(len(modp)):
    print("T_" + str(n) + " = " + poly(modp[n]))
    print('')

# Calculating the derivative #
if yes:
    derivp = p.copy()
    for n in range(len(derivp)):
        for e in range(len(derivp[n])):
            derivp[n][e] = derivp[n][e] * e
        derivp.pop(0)

        print('')
        for n in range(len(derivp)):
            print("T_" + str(n) + " = " + poly(derivp[n]))
            print('')

import random
import numpy as np

def incrementIndexOfMultidimentionalTable(tab, idx_tab):
    last_idx = idx_tab.__len__()-1
    if len(idx_tab) != 1:
        return incrementIndexOfMultidimentionalTable(tab[idx_tab[last_idx]], idx_tab[:last_idx])
    tab[idx_tab[last_idx]] += 1
    return tab[idx_tab[last_idx]]

def getNumberWithPropability(tab):
    rand = random.random()
    last_pi = 0
    for i in range(len(tab)):
        if rand < tab[i] + last_pi:
            return i
        last_pi += tab[i]
    return len(tab)

def getMultidimentionalWithPropability(tab):
    # P(A|B) = P(A ^ B) / P(B)
    # prob_a_b = () / prob_b
    prob_b = tab.sum()
    prob_a_b = [0]*tab.shape[0]
    for i in range(tab.shape[0]):
        prob_a_b[i] = tab[i].sum() / prob_b
    rand_idx = getNumberWithPropability(prob_a_b)
    if len(tab.shape) != 1:
        multidimentional = getMultidimentionalWithPropability(tab[rand_idx])
        multidimentional.append(rand_idx)
        return multidimentional
    return [rand_idx]


arr = np.array([[0, 0.1, 0, 0],
                [0.1, 0, 0.2, 0],
                [0, 0.2, 0, 0.15],
                [0, 0, 0.15, 0.1]])

wartosci = np.zeros(arr.shape)
for _ in range(100000):
    x = getMultidimentionalWithPropability(arr)
    incrementIndexOfMultidimentionalTable(wartosci, x)
print(wartosci)
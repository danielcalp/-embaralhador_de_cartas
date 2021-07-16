def bubbleSort(v):
    for i in range(0, len(v)-1):
        for j in range(0, len(v)-1-i):
            if v[j] > v[j+1]:
                temp = v[j]
                v[j] = v[j+1]
                v[j+1] = temp


RA = [1, 9, 0, 3, 1, 7, 6]

bubbleSort(RA)

def troca(v,p1,p2)

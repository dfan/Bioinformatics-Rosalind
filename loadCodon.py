codons = open('codonTable.txt', 'r')

def codonTable():
    j = 0
    # dictionary (like a symbol table)
    codonTable = {}
    for line in codons:
        params = line.rstrip('\n').split(' ')
        codonTable[params[0]] = params[1]
        j += 1
    return codonTable
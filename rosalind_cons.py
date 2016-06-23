data = open('rosalind_cons.txt', 'r')

freqTab = {'A': [], 'C': [], 'G': [], 'T': []}
string = ''

while True:
    line = data.readline().rstrip('\n')
    if line == '' or line[0] == '>':
        for i in range(0, len(string)):
            if len(freqTab[string[i]]) <= i:
                freqTab['A'].append(0)
                freqTab['C'].append(0)
                freqTab['G'].append(0)
                freqTab['T'].append(0)
            freqTab[string[i]][i] += 1
        string = ''
        if line == '':
            break
    else:
        string += line

# print consensus string
consensus = ''
for i in range(0, len(freqTab['A'])):
    vals = [freqTab['A'][i], freqTab['C'][i], freqTab['G'][i], freqTab['T'][i]]
    consensus += sorted(freqTab.keys())[vals.index(max(vals))]
print consensus

# print in alphabetical order
for key in sorted(freqTab):
    print key + ":",
    print " ".join(map(str, freqTab[key]))
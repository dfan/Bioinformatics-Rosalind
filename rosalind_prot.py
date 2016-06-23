from loadCodon import codonTable

data = open('rosalind_prot.txt', 'r')
codons = codonTable()
protein = ''

dna = data.readline().rstrip('\n')
for i in range(0, len(dna), 3):
    if codons[dna[i : i + 3]] != 'Stop':
        protein += codons[dna[i : i + 3]]

print protein
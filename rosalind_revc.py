data = open('rosalind_revc.txt', 'r')
s = data.readline()
sc = ""

for i in range(len(s) - 1, -1, -1):
    if s[i] == "A":
        sc += "T"
    if s[i] == "C":
        sc += "G"
    if s[i] == "G":
        sc += "C"
    if s[i] == "T":
        sc += "A"
print sc
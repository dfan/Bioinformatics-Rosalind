data = open('rosalind_rna.txt', 'r')
t = list(data.readline())

# strings are immutable, work with string as list
for i in range(0, len(t)):
    if t[i] == "T":
        t[i] = "U"
print "".join(t)
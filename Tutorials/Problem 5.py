f = open('rosalind_ini5.txt', 'r')
i=0
j=1
for line in f:
    i=i+1
print i
print f.readline()[5]
while j<=i:
    f.readlines()[j]
    j=j+2

    

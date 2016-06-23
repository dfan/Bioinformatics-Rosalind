original = open('rosalind_hamm.txt', 'r')
str1 = original.readline().rstrip('\n')
str2 = original.readline().rstrip('\n')

hammingDist = 0
for i in range(0, len(str1)):
    if str1[i] != str2[i]:
        hammingDist += 1

print hammingDist
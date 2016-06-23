original = open('rosalind_gc.txt', 'r')

highestID = ''
currentID = ''
currentString = ''
highestGC = 0.0

while True:
    line = original.readline().rstrip('\n')
    if (len(line) == 0 or line[0] == '>'):
        if (len(currentString) != 0 and float(currentString.count('G') + currentString.count('C')) / len(currentString) >= highestGC):
            highestID = currentID
            highestGC = float(currentString.count('G') + currentString.count('C')) / len(currentString)
        if (len(line) == 0):
            break
        currentID = line
        currentGC = 0.0
        currentString = ''
    else:
        currentString += line

print highestID[1:len(highestID)]
print highestGC * 100
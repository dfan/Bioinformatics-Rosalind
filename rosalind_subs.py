data = open('rosalind_subs.txt', 'r')

s = data.readline().rstrip('\n')
t = data.readline().rstrip('\n')
locations = []

for i in range(0, len(s)):
    if s[i : i + len(t)] == t:
        locations.append(i + 1)
print ' '.join(map(str, locations))
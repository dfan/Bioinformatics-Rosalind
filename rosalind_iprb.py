data = open('rosalind_iprb.txt', 'r')
params = data.readline().split(' ');
k = int(params[0])
m = int(params[1])
n = int(params[2])

kk = float(k) / (k + m + n) * float(k - 1) / (k + m + n - 1)
km = float(k) / (k + m + n) * float(m) / (k + m + n - 1)
kn = float(k) / (k + m + n) * float(n) / (k + m + n - 1)
mk = float(m) / (k + m + n) * float(k) / (k + m + n - 1)
mm = float(m) / (k + m + n) * float(m - 1) / (k + m + n - 1)
mn = float(m) / (k + m + n) * float(n) / (k + m + n - 1)
nk = float(n) / (k + m + n) * float(k) / (k + m + n - 1)
nm = float(n) / (k + m + n) * float(m) / (k + m + n - 1)
nn = float(n) / (k + m + n) * float(n - 1) / (k + m + n - 1)

print kk + km + kn + mk + mm * 0.75 + mn * 0.5 + nk + nm * 0.5
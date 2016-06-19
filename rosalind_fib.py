data = open('rosalind_fib.txt', 'r')
params = data.readline().split(' ');
n = int(params[0])
k = int(params[1])

Fn_1 = 1
Fn_2 = 1
prev = 0
# pairs of offspring in a month = pairs of rabbits alive two months before
# Fn = Fn_1 + Fn_2; counted in pairs

def fib(n, k):
    global Fn_1
    global Fn_2
    global prev
    if n == 2:
        return Fn_2
    prev = Fn_1
    Fn_1 = Fn_2
    Fn_2 = prev * k + Fn_1
    return fib(n - 1, k)

print fib(n, k)
from math import exp, factorial
from numpy import cumsum

def aitken(s0, s1, s2):
    return s2 - (s2 - s1)**2/(s2 - 2*s1 + s0)

def exp_partial_sums(x, N):
    terms = [x**n/factorial(n) for n in range(N)]
    return cumsum(terms)

x, N = 0.3, 6
partial = exp_partial_sums(x, N)

# estimate taking the last partial sum
p = partial[-1]

# estimate applying Aitken acceleration
a = aitken( partial[-3], partial[-2], partial[-1] )

# error analysis
error_p = exp(x) - p
error_a = exp(x) - a
print(error_p, error_a, error_p/error_a)
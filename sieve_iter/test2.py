import sieve

for n, i in zip(range(1), sieve.sieve()):
    print i
    
assert i == 3

print "Test 2 Worked!"
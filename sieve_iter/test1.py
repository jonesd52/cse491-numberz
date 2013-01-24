import sieve

for n, i in zip(range(10), sieve.sieve()):
    print i
    
assert i == 31

print "Test 1 Worked!"
import sieve

for n, i in zip(range(30), sieve.sieve()):
    print i
    
assert i == 127

print "Test 3 Worked!"
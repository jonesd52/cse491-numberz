last_1 = 1 		# define last_1 as 1
last_2 = 1		# define last_2 as 1

def next():
    global last_1, last_2

    next_fib = last_1 + last_2			# set the next fib as the previous two fibonaccci numbers
    last_1, last_2 = last_2, next_fib		# define last_1 as last_2, and set last_2 as next_fib
    
    return next_fib				# print out the last_fib number

print next()
print next()
print next()

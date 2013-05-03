#! /usr/bin/env python3.3
theSum = 0
for n in range(1,1000):
	if n%3 == 0 or n%5 == 0:
		theSum += n
print("The sum of all integers below 1000 that are multiples of 3 or 5 is: "+ str(theSum))

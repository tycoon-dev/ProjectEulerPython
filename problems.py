def problem1():
	total = 0
	for x in range(1000):
		if (x % 3 == 0) or (x % 5 == 0):
			total = total + x
	
	return total	

def problem3():
	
	x = 13195
	
	for y in range(x-1, 1,-1):
		if(x % y == 0):
			return y;
			
def problem5():
	hasFound = False
	counter = 0
	i = 20

	while hasFound == False:

		for x in range(1,21):
			
			if (i % x == 0):
				counter = counter + 1
				if (counter == 20):
					hasFound = True
					break
					
			else:
				counter = 0
				i = i + 1
				
	return i			
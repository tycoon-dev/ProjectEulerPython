def problem1():
	total = 0
	for x in range(1000):
		if (x % 3 == 0) or (x % 5 == 0):
			total = total + x
	
	return total	

def problem3():
	
	
	
	valor = 63400
	y = []
	p = 2
	hasFound = False
	
	for x in range(0,valor):
		y.append(False)
		
	while(hasFound == False):
		for z in range(2, valor, 1):
			if(z*p < valor):
				if (y[z*p] == False):
					y[z*p] = True
					
					
				
		
		for x in range(2, valor, 1):
			if((x > p) and (y[x] == False)):
				p = x
				break
			elif(x == valor-1):
				hasFound = True
			
			
	
	for a in range (valor-1, 0, -1):
		if (y[a] == False):
			return a;
			
		
			
		
	
	
	
	
			
			
			
			
			
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
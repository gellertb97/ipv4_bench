#!/usr/bin/env python3

from datetime import datetime

if __name__ == "__main__":

	# start time
	startTime = datetime.now()
	
	ip = [0,0,0,0]
	
	while ip[0] < 255:
		while ip[1] < 255:
			ip[1] += 1
			while ip[2] < 255:
				while ip[3] < 255:
					ip[3] += 1
					#print(str(ip[0]) + '.' + str(ip[1]) + '.' + str(ip[2]) + '.' + str(ip[3]))
				ip[2] += 1
				ip[3] = 0
				#print(str(ip[0]) + '.' + str(ip[1]) + '.' + str(ip[2]) + '.' + str(ip[3]))
			ip[1] += 1
			ip[2] = 0
			#print(str(ip[0]) + '.' + str(ip[1]) + '.' + str(ip[2]) + '.' + str(ip[3]))		
		ip[0] += 1
		ip[1] = 0
		#print(str(ip[0]) + '.' + str(ip[1]) + '.' + str(ip[2]) + '.' + str(ip[3]))	
		
	
	runTime = datetime.now() - startTime
	runTime = runTime.seconds / 60
			
	print("Done!\n\n")
	
	print('Executed in ' + str(runTime) + ' minutes.')

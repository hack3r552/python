#!/usr/bin/env python

import socket,threading,time,thread


class port_scan(threading.Thread):
	openportcount=0
	def __init__(self,host,portrange):
		threading.Thread.__init__(self)
		self.hostname=host
		self.portrange=portrange
	def run(self):
		
		while True:
			
			for port in range(self.portrange[0],self.portrange[1]):
				sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				sock.settimeout(1)
				result=sock.connect_ex((self.hostname,port))
				if result == 0:
					
					print '\t\t[@]  port {0}    :    open    :    {1}'.format(port,socket.getservbyport(port))
					port_scan.openportcount+=1
				else:
					pass
				sock.close()
				
			thread.exit()
def main():
	
	print '\n\nStarting port scanner...\n'
	host = raw_input('[?] Host name for port scanning :>')
	portrange=list((raw_input("[?] Port range :> ").split('-')))
	threads=[]
	lport = int(portrange[0])
	uport = int(portrange[1])
	div= int((lport+uport)/2)
	mlport=lport+div
	muport=mlport+1
	ports1=[lport,mlport]
	ports2=[muport,uport]
	tm=time.time()
	thread1=port_scan(host,ports1)
	thread1.start()
	threads.append(thread1)
	thread2=port_scan(host,ports2)
	thread2.start()
	threads.append(thread2)
	
	for t in threads:
		t.join()
	print (time.time()-tm)/2,' Seconds'
	print'\n%d ports open'%port_scan.openportcount
	print'Done'
	print 'Total threads : {0}'.format(len(threads))
	print threads

if __name__ == '__main__':
	main()
	
		

































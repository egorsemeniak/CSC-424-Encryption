#!/usr/bin/env python
import socket
import time
import os
import sys
###############################################################################################
def tcpConnect ( port ):
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	soc.bind(('',port)) 
	soc.listen( 1 ) 
	soc, addr = soc.accept()
	return soc
###############################################################################################
def tcpWrite( soc, sData):
   soc.sendall(sData)
   return 
###############################################################################################
def tcpRead(  soc ):
	receivedData = soc.recv ( 16 )
	return receivedData
###############################################################################################
def tcpClose(  soc ):
   soc.close()
   return 
###############################################################################################
def main (ip, port):
	soc = tcpConnect ( int(port) )
	#
        # encryption code goes here
        # put encrypted string into
        # soc.recv (16) - will read from the socket
        # 16 bytes, encryption in 16 byte block
        #
	while ( True ):
	  clientSent = tcpRead( soc )
	  print 'Server received ' + clientSent

	  if 'quit' in clientSent:
            tcpClose( soc )
	    exit ( -1 )
	  #
	  # decrypt code  here 
	  #
	  tcpWrite( soc, clientSent.upper() )
###############################################################################################
###############################################################################################
if __name__ == "__main__":
        print sys.argv[1:]
        #argv[1] is ip can be localhost, argv[2] is the port
        main (sys.argv[1], sys.argv[2])
###############################################################################################
###############################################################################################

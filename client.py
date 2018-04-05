#!/usr/bin/env python
import socket, time, sys
import time
import sys
###############################################################################################
def tcpConnect( ip, port ):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((ip, int(port)))
    return soc
###############################################################################################
def tcpWrite( soc, sData):
   if  len( sData ) != 16:
            sData  += ' ' *  (16 - (len(sData ) % 16))
   soc.send( sData )
   return 
###############################################################################################
def tcpRead( soc ):
	serverSent = soc.recv( 16 )
	return  serverSent
###############################################################################################
def tcpClose( soc ):
   soc.close()
   return 
###############################################################################################
def main ( ip, port):
	soc = tcpConnect( ip, port )
	while ( True ):
	  cInput = raw_input ("Enter a Message to Encrypt ")
	  #
          # encryption code goes
	  # put encrypted string into 
	  # cInput must be terminated with a '\r'
	  # because tcpRead in the client/server code
	  # scans for a \r to stop
	  # we can change the recc to read blocks
	  # s.recv (16) - will read from the socket
	  # 16 bytes
	  #
	  if cInput == "quit":
	   tcpWrite ( soc, cInput  )
	   tcpClose ( soc )
	   exit ( -1 )

	  tcpWrite ( soc, cInput )
	  sInput =  tcpRead( soc )
          print 'Client Received ' + sInput
	tcpClose()
###############################################################################################
###############################################################################################
if __name__ == "__main__":
        print sys.argv[1:]
        #argv[1] is ip can be localhost, argv[2] is the port
        main (sys.argv[1], sys.argv[2])
###############################################################################################
###############################################################################################

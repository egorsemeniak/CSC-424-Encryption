#!/usr/bin/env python
import socket
import time
import os
import sys
import random
from Crypto.Hash import SHA256
from Crypto.Cipher import AES


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
	receivedData = soc.recv ( 300 )
	return receivedData
###############################################################################################
def tcpClose(  soc ):
   soc.close()
   return 
###############################################################################################
def main (ip, port):
	soc = tcpConnect ( int(port) )
	



	while ( True ):
	  clientSent = tcpRead( soc )
    	  if 'quit' in clientSent:
            tcpClose( soc )
	    exit ( -1 )
	  print 'Server received ' + clientSent
  	  print "*******************************************"
	  print "***********BREAKING DOWN DATA**************"
	  print "*******************************************"
	  Received_Data = clientSent.split("\x20")
	  print "Number of Initial Bytes: ",(Received_Data[3])
	  print "Key: ",(Received_Data[2])
	  print "Password: ",(Received_Data[1])
	  print "Data: ",(Received_Data[0])
	  print len(Received_Data[0])
	  i = int(Received_Data[3])
	  Decryptor = AES.new(Received_Data[1], AES.MODE_CBC,Received_Data[2])
	  encrypted_string =""
	  encrypted_string = Received_Data[0];
	  decrypted_string =""
	  decrypted_string =""
	  decrypted_string =(Decryptor.decrypt(encrypted_string))[0:i]
	  print"*******************************************"
	  print "**Message: ",decrypted_string
	  print"*******************************************"

	
	 

	  tcpWrite( soc, decrypted_string)
###############################################################################################
###############################################################################################
if __name__ == "__main__":
        print sys.argv[1:]
        #argv[1] is ip can be localhost, argv[2] is the port
        main (sys.argv[1], sys.argv[2])
###############################################################################################
###############################################################################################

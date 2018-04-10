#!/usr/bin/env python
import socket, time, sys
import time
import sys
import os, random
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import MySQLdb

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
	serverSent = soc.recv( 500 )
	return  serverSent
###############################################################################################
def tcpClose( soc ):
   soc.close()
   return 
###############################################################################################
def SQL_Execute(arg):
    db = MySQLdb.connect (host = "localhost", user = "root", passwd = "root", db = "classicmodels")
    cur = db.cursor()
    cur.execute(arg)
    for row in cur.fetchall():
        print row
    db.close()
###############################################################################################

def main ( ip, port):
	soc = tcpConnect( ip, port )
	while ( True ):
    		


	  		cInput = raw_input ("Enter a Message to Encrypt ")

	  		if cInput == "quit":
    	   			tcpWrite ( soc, cInput)
	   			tcpClose ( soc )
	   			exit ( -1 )


	 		password = raw_input("Enter the password: ")
	 		password = SHA256.new(password).digest()
	  		randomKey = ''
			ToServer = ""
	  		for i in range(16):
    				randomKey += chr(random.randint(0, 0xFF))
	 		encryptor = AES.new(password, AES.MODE_CBC, randomKey)
			
			print "**********************************************************"
			print "***************BEFORE ENCRYPTION**************************"
			print "**********************************************************"
	  		print '* Random Key:'
	 		print(randomKey)
	  		print '* Password:'
	  		print(password)
	 		print '* Message:'
	 		print(cInput)
			print "**********************************************************"

			initial_length = 0
			initial_length = len(cInput)

			if len(cInput) % 16 !=0:
    				cInput  += 'Y' *  (16 - (len(cInput) % 16))
			print "After Padding: "
			print (cInput)
			length = "%05d" % (len(cInput))
			Encrypted_String = encryptor.encrypt(cInput)
			print "**********************************************************"
			print "Data That is Being Sent:"
			print "Initial Length: " , initial_length
			print "Random Key: " , randomKey
			print "Password: " , password
			print "Encrypted String: " , Encrypted_String
			print "Size of ES: ",len(Encrypted_String)
			print "**********************************************************"
			#SendToServer = "%05d:%s:%s:%s" % (initial_length, randomKey, password, Encrypted_String)
			SendToServer = "%s\x20%s\x20%s\x20%05d" % ( Encrypted_String, password, randomKey,initial_length)

	  		tcpWrite ( soc, SendToServer )
	  		sInput =  tcpRead( soc )
			print"SQL RESULTS: "
			SQL_Execute(sInput)
        		#print 'Client Received ' + sInput
	tcpClose()
###############################################################################################
###############################################################################################
if __name__ == "__main__":
        print sys.argv[1:]
        #argv[1] is ip can be localhost, argv[2] is the port
        main (sys.argv[1], sys.argv[2])
###############################################################################################
###############################################################################################

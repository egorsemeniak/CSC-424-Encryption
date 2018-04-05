# CSC 424 Encryption
Assignment:

Background: As introduced in lab 1, modern databases are architected to operate in a client/server paradigm. In lab 1 we modified ‘C’ client/server code. The client code could connect to the server code from any location supporting network access (ip/port). The client interface is extremely flexible. Commands can be entered from the client connection passing queries to create databases, interrogate tables and execute DDL and DML.

Consider any web page with a database backend. Entering database commands from a command line interface is not feasible. Therefore, programmatic facilities must be provided. There are many languages supporting MySQL databases and tables access. For example, Java using a Java Database Connector (JDBC). There are also interfaces many other languages like C API, Perl DBI, the PHP API, the Connector/Python, and the Ruby API.

Client applications can be executed on the east code of the United States connecting to a server in Australia. Consider what could occur is data is transmitted by satellite and someone, possibly a spy or a hacker or a simply a criminal listening. An even more likely possibility is that someone within the organization seeks to steal content. The target could be social security numbers or bank accounts numbers. Whatever the target data, encrypted data is far less likely to be comprised.

In lab3 you will modify the python client/server code found on blackboard to encrypt mysql select statement, send the statement to the server and decrypt the request, execute the decrypted statement on the server and send the request back to the client. (Note: In a real-world application, data returned from server and sent back to the client would also be encrypted before being transmitted and de-crypted on the client.)

Python
Install python encryption using “pip install pycrypto”

from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import os
random, sys
_______________________________________________
encrypt in 16 byte chunks
enter a password or a key (key=input(“message)
randomKey = ''
for i in range(16):
randomKey += chr(random.randint(0, 0xFF))
encryptor = AES.new(password, AES.MODE_CBC, randomKey)

encryptedString = ‘’
build an encrypted string for every 16 byte of data  (16bytesOfData)
encryptedString += execute encryptor.encrypt(16bytesOfData)

since we are encrypting 16 bytes at a time then the length of the string must be the first 16 bytes and the randomKey is the second 16 bytes (do not encrypt these data)

stringSize = len(stringName)).zfill(16)
following the string size write the 16 byte randomKey
_______________________________________________
expand to 16 bytes
someString less that 16 bytes
someString += ' ' *  (16 - (len(someString) % 16))

de-crypt in 16 byte chunks
enter the same password as you used to encrypt
decryptor = AES.new(key, AES.MODE_CBC, randomKey)
the length of the string and the randomKey are read processed first using python index
length = encryptedString [0:16]
randomkey =  encryptedString [16:32]

decryptor = AES.new(password, AES.MODE_CBC, randomKey)

for each 16 bytes
decryptedString = ‘’
build a decrypted string for every 16 byte of data
decryptedString = execute encryptor.encrypt(16bytesOfData)

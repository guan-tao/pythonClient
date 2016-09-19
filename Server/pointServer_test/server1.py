# -*- coding: cp936 -*-
from socket import *
import struct
import threading
import time

buf =''
with open(r"..\..\2016-5-7-16\Test_data\point0_00_00\CSI00_00.dat","rb") as file:
    while True:
        bytex = file.readline()
        if  bytex:
            buf +=  bytex
            #print bytex.encode('string-escape')
        else:
            break
bufCopy = buf[:]
        
HOST = ''
PORT = 10001
ADDR = (HOST,PORT)
BUFSIZ = 1024*1024*5
server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDR)
server.listen(5)
print "等待连接..\n"

def process(buf,bufCopy,client,addr):    
    while True:
        sendstr = buf[:43000]
        if( len(buf) > 43000 ):
            buf = buf[43000:]
            client.send(sendstr)
            time.sleep(1)
        else:
            buf = bufCopy[:]
            time.sleep(1) 

while True:
    client,addr = server.accept()
    print "连接成功..\n"
    t = threading.Timer(1,process,args=(buf,bufCopy,client,addr))
    t.start()

            

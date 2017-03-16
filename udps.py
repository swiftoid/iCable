#!/usr/bin/python
import sys
import socket
import os

def main():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost',80))
    clientsocket.send('hello')
    print "sent"
main()

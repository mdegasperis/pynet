#! /usr/bin/env python

import telnetlib
import time
import socket
import sys
import getpass



class Telnet(object):
    def __init__(self, ip, username, password, port, timeout, cmd):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout
        self.cmd = cmd

    def connect(self):
        # Establish connection to network device
        try:
            remote_conn = telnetlib.Telnet(self.ip, self.port, self.timeout)
        except socket.timeout:
            sys.exit("Connection timed out")
        
        # Authenticate
        output = remote_conn.read_until("sername:", self.timeout)
        remote_conn.write(self.username + "\n")
        output = remote_conn.read_until("assword:", self.timeout)
        remote_conn.write(self.password + "\n")
        output = remote_conn.read_very_eager()

        # Disable paging
        remote_conn.write("terminal length 0\n")
        output = remote_conn.read_very_eager()
        return output






def main():
    TELNET_PORT = 23
    TELNET_TIMEOUT = 6
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = '88newclass'
    command = 'show version'

    remote_conn = Telnet(ip_addr, username, password, TELNET_PORT, TELNET_TIMEOUT, command)
    
    output = remote_conn.connect()
    print output

if __name__ == '__main__':
    main()

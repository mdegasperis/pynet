#! /usr/bin/env python

import telnetlib
import time
import socket
import sys
import getpass


# Convert Telnet code created by Kirk from using functions to classes.


class TelnetConnection(object):
    def __init__(self, ip, username, password, port, timeout):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout
    
    def login(self):
        try:
            self.remote_conn = telnetlib.Telnet(self.ip, self.port, self.timeout)
        except socket.timeout:
            sys.exit("Connection timed out")

        # Authenticate
        output = self.remote_conn.read_until("sername:", self.timeout)
        self.remote_conn.write(self.username + "\n")
        output = self.remote_conn.read_until("assword:", self.timeout)
        self.remote_conn.write(self.password + "\n")
        output = self.remote_conn.read_very_eager()

        # Disable paging
        self.remote_conn.write("terminal length 0\n")
        output = self.remote_conn.read_very_eager()
        return output

class Telnet(TelnetConnection):
    def __init__(self, cmd='', ip='', username='', password='', port='', timeout=''):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout
        self.cmd = cmd

        # TelnetConnection.__init__(self, ip, username, password, port, timeout)        
        self.remote_conn = TelnetConnection(self.ip, self.username, self.password, self.port, self.timeout)
        

        self.remote_conn.login()
        #return self.remote_conn

    def send(self, cmd):
        #cmd = self.cmd
        cmd = cmd.rstrip()
        self.remote_conn.remote_conn.write(cmd + '\n')
        time.sleep(1)
        return self.remote_conn.remote_conn.read_very_eager()



def main():
    port = 23
    timeout = 6
    ip = '50.76.53.27'
    username = 'pyclass'
    password = '88newclass'
    command = 'show version'

    remote_conn = Telnet(command, ip, username, password, port, timeout)
    
    output = remote_conn.send('show ip int brief')
    print output

if __name__ == '__main__':
    main()

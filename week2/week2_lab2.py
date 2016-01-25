#! /usr/bin/env python

import time
from telnetlib import Telnet

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():

    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = '88newclass'

    # Establish Connection
    remote_conn = Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    # Read output, until Username
    output = remote_conn.read_until('sername', TELNET_TIMEOUT)
    # Enter username
    remote_conn.write(username + "\n")
    # Read output, until password
    output = remote_conn.read_until('assword', TELNET_TIMEOUT)
    # Enter password
    remote_conn.write(password + "\n")
    # Read output
    output = remote_conn.read_very_eager()
    
    
    # Enter terminal length command
    remote_conn.write("terminal length 0\n")
    time.sleep(1)
    output = remote_conn.read_very_eager()

    # Enter show ip int brief command
    remote_conn.write("show ip int brief" + "\n")
    time.sleep(1)

    # Read output
    output = remote_conn.read_very_eager()
    
    print output




if __name__ == '__main__':

    main()


#! /usr/bin/env python

import pexpect

def int_brief():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    port = 8022
    password = '88newclass'


    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))

    #ssh_conn.logfile = sys.stdout

    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)

    ssh_conn.expect('#')

    ssh_conn.sendline('show ip int brief')
    ssh_conn.expect('#')

    print ssh_conn.before



def change_logging():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    port = 8022
    password = '88newclass'


    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))

    #ssh_conn.logfile = sys.stdout

    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)

    ssh_conn.expect('#')

    ssh_conn.sendline('conf t')
    ssh_conn.expect('#')

    ssh_conn.sendline('logging buffered 55055')
    ssh_conn.expect('#')

    ssh_conn.sendline('end')
    ssh_conn.expect('#')

    ssh_conn.sendline('show run | i logging buff')
    ssh_conn.expect('#')
    print ssh_conn.before





if __name__ == '__main__':
    print
    int_brief()
    print
    print
    change_logging()
    print


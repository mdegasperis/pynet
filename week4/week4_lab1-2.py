#! /usr/bin/env python

import paramiko
import time


def connect(command, ip, user, passwd, port=22):

    remote_conn_pre = paramiko.SSHClient()

    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    remote_conn_pre.connect(ip, username=user, password=passwd, look_for_keys=False, allow_agent=False, port=port)

    remote_conn = remote_conn_pre.invoke_shell()

    output = remote_conn.recv(5000)
    time.sleep(1)
    
    output = remote_conn.send('terminal length 0\n')
    time.sleep(1)
    output = remote_conn.recv(65535)


    for cmd in command:
        output = remote_conn.send(cmd + '\n')
        time.sleep(1)

        output = remote_conn.recv(65535)

    return output



def show_ver():

    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = '88newclass'
    port = 8022
    cmd_list = ['show version']

    connection = connect(cmd_list, ip_addr, username, password, port)
    print connection


def change_logging():

    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = '88newclass'
    port = 8022
    cmd_list = ['config t', 'logging buffered 51212', 'end', 'show run | i logging']

    connection = connect(cmd_list, ip_addr, username, password, port)
    print connection


if __name__ == '__main__':


    print
    show_ver()
    print
    print
    change_logging()
    print

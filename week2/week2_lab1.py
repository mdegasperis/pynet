#! /usr/bin/env python

import pysnmp
import paramiko
import my_func


def print_ver():

    print "\nPySNMP Version: %s" % (pysnmp.__version__)

    print "Paramiko Version: %s\n" % (paramiko.__version__)


if __name__ == '__main__':

    print_ver()

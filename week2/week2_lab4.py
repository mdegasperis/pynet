#! /usr/bin/env python

from snmp_helper import snmp_get_oid,snmp_extract
import getpass


def main():
    '''
    Prompt user for IP address and community string. 
    Returns output for SysDescr and SysName MIBs.
    '''
    # For reference
    
    # ip_addr = '50.76.53.27'
    # community = 'galileo'

    
    # Prompt for IP address and sanitize of trailing spaces

    ip_addr = raw_input("Please enter an IP: ")
    ip_addr = ip_addr.strip()

    
    # Prompt for community string, text will be masked using getpass

    community = getpass.getpass(prompt="Enter Community String: ")

    
    # Tuples for each router
    
    rt1 = (ip_addr, community, 7961)
    rt2 = (ip_addr, community, 8061)
    
    
    # List of routers
    
    device_list = [rt1, rt2] 
    
    
    # List of OIDS: SysName, SysDescr
    
    oid_list = ['1.3.6.1.2.1.1.5.0', '1.3.6.1.2.1.1.1.0']

    
    for device in device_list:
        
        print "\n********************"

        for oid in oid_list:
            
            snmp_data = snmp_get_oid(rt1, oid)
            output = snmp_extract(snmp_data)
            
            print output
        
        print "********************"

    print



if __name__ == '__main__':
    main()

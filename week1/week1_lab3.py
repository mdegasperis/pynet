#! /usr/bin/env python

from ciscoconfparse import CiscoConfParse


def cmap_crypto(config):
    '''
    Accepts a Cisco config file and prints all crypto maps 
    titled CRYPTO.
    '''


    # Create CiscoConfParse object with config passed into function.
    cisco_cfg = CiscoConfParse(config)
    
    
    # Find config lines matching string below.
    cmap = cisco_cfg.find_objects(r'^crypto map CRYPTO')
    

    # Iterate over lines matched previously. Print the line.
    for seq_num in cmap:
        print seq_num.text

        # Iterate over children of the config line, print children. 
        for child in seq_num.children:
            print child.text




def pfs_group2(config):
    '''
    Accepts CiscoConfParse object consisting of a list
    of crypto map entries in a cisco config file.
    '''
    

    # Create CiscoConfParse object with config passed into function.
    cisco_cfg = CiscoConfParse(config)
    
    
    # Find only crypto maps using pfs group 2
    pfs2 = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")

    
    # Iterate over lines matched previously. Print the line. 
    for seq_num in pfs2:
        print seq_num.text
    
        # Iterate over children of the config line, print children. 
        for child in seq_num.children:
                print child.text


def main():
    '''
    Main Program
    '''


    # Create config file object.
    config = "cisco_ipsec.txt"


    # Call function to print and return all crypto maps.
    print "\n\n---------- All Crypto Maps ----------\n"
    crypto_map = cmap_crypto(config)
    

    # Call function to return only crypto maps using pfs group 2.
    print "\n\n------------ Only PFS 2 ------------\n"
    pfs_2 = pfs_group2(config)



if __name__ == '__main__':

    main()
    

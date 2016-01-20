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

    


def main():
    '''
    Main Program
    '''

    # Create config file object.
    config = "cisco_ipsec.txt"
    
    # Call function to print all crypto maps.
    cmap_crypto(config)
    


if __name__ == '__main__':

    main()
    

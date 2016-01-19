#! /usr/bin/env python

import yaml
import json
from pprint import pprint

def yaml_write(a_list):
    '''
    Accepts a list and creates YAML file in 
    expanded format.
    '''

    with open("week1_lab2.yml", "w") as file:
        file.write(yaml.dump(a_list, default_flow_style=False))
    


def yaml_read(yaml_file):
    '''
    Accepts input of YAML file and returns
    file contents in a list.
    '''

    with open(yaml_file) as file:
        yaml_list = yaml.load(file)
        return yaml_list



def json_write(a_list):
    '''
    Accepts a list and creats a JSON file.
    '''

    with open("week1_lab2.json", "w") as file:
        json.dump(a_list, file)



def json_read(json_file):
    '''
    Accepts input of JSON file and returns
    file contents in a list.
    '''

    with open(json_file) as file:     
        json_list = json.load(file)
        return json_list


def main():

    yaml_file = "week1_lab2.yml"
    json_file = "week1_lab2.json"
    
    lab_list = ['cisco', 'pynet', 'yaml', 'json', {'hostname': 'DEG-SW1', 'ip_addr': '10.120.1.1', 'model': 'C891F-K9'}]


    # Write both files using the lab_list
    yaml_write(lab_list)
    json_write(lab_list)

    # Read from files and store in variable
    yaml_list = yaml_read(yaml_file)
    json_list = json_read(json_file)

    # Print list from YAML file
    print
    print "---------- Printed from YAML ----------\n"
    pprint(yaml_list)
    print
    print
    # Print list from JSON file
    print "---------- Printed from JSON ----------\n"
    pprint(json_list)
    print



if __name__ == '__main__':

    main()

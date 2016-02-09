#! /usr/bin/env python

import snmp_helper
from pprint import pprint
import pickle
import email_helper


def uptime(hsecs):
    '''
    Accepts an integer as hundredths of seconds and
    converts it to seconds.
    '''
    seconds = hsecs / 100

    if seconds >= 60:
        minutes = seconds / 60
        seconds = seconds % 60
    else:
        minutes = 0

    return minutes,seconds


def send_email(change_time):

    minutes,seconds = uptime(change_time)

    recipient = 'mike@degasperis.ca'
    subject = 'Config Changed!'
    message = '''

The routers running configuration has changed %s minutes and %s seconds ago.

Thanks,
Config-change-automailer
    ''' % (minutes, seconds)


    sender = 'noreply@degasperis.ca'
    email_helper.send_mail(recipient, subject, message, sender)


def last_changed():
    IP = '50.76.53.27'
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (a_user, auth_key, encrypt_key)
    pynet_rtr1 = (IP, 7961)
    pynet_rtr2 = (IP, 8061)
    pickle_file = "last_changed.pkl"

    # Define OIDs to get data for
    snmp_oids = (
        ('sysUptime', '1.3.6.1.2.1.1.3.0'),
        ('ccmHistoryRunningLastChanged', '1.3.6.1.4.1.9.9.43.1.1.1.0'),
        ('ccmHistoryRunningLastSaved', '1.3.6.1.4.1.9.9.43.1.1.2.0'),
        ('ccmHistoryStartupLastChanged', '1.3.6.1.4.1.9.9.43.1.1.3.0')
        )


    # Create empty dictionary with OID descriptions as keys
    change_dict = {'sysUptime': "", 'ccmHistoryRunningLastChanged': "", 'ccmHistoryRunningLastSaved': "", 'ccmHistoryStartupLastChanged': ""}


    # Run through snmp_oids tuple, store recieved values in change_dict
    for desc,an_oid in snmp_oids:
        snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid=an_oid)
        output = snmp_helper.snmp_extract(snmp_data)
        change_dict[desc] = output


    # Read current contents of pickle_file as previous snmp reading
    snmp_file = open(pickle_file, "rb")
    prev_read = pickle.load(snmp_file)
    
    
    # Compare values of snmp readings, if the current value is less than the stored value a reload has occurred
    #if int(change_dict['sysUptime']) <= int(prev_read['sysUptime']):
    #    print "\nSystem has reloaded since last poll."
    
    #else:
    #    print "\nSystem has not reloaded since last poll."

    
    # Compare values 
    if int(change_dict['ccmHistoryStartupLastChanged']) == 0 and int(change_dict['ccmHistoryRunningLastSaved']) == 0:
        return False
 
    elif int(change_dict['ccmHistoryRunningLastChanged']) > int(prev_read['ccmHistoryRunningLastChanged']):
        change_time = int(change_dict['ccmHistoryRunningLastChanged']) - int(prev_read['ccmHistoryRunningLastChanged'])
        send_email(change_time)
        return True

    else:
        return False            




    snmp_file = open(pickle_file, "wb")
    pickle.dump(change_dict, snmp_file)
    snmp_file.close()


if __name__ == '__main__':
    if last_changed():
        print "\nRunning config has changed!\n"
    else:
        print "\nRunning config has not changed since last poll.\n"


#! /usr/bin/env python

import pygal
import snmp_helper
from pprint import pprint
import time

def intf_data():

    IP = '50.76.53.27'
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (a_user, auth_key, encrypt_key)
    pynet_rtr1 = (IP, 7961)
    pynet_rtr2 = (IP, 8061)

    snmp_oids = (
        ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5'),
        ('ifInOctects_fa4', '1.3.6.1.2.1.2.2.1.10.5'),
        ('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5'), 
        ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
        ('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')
        )

    iface_dict = {'ifDescr_fa4': "", 'ifInOctects_fa4': [], 'ifInUcastPkts_fa4': [], 'ifOutOctets_fa4': [], 'ifOutUcastPkts_fa4': []}


    for i in range(0, 65, 5):

        for desc,oid in snmp_oids:
            snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=oid)
            output = snmp_helper.snmp_extract(snmp_data)
        
            if 'ifDescr' in desc:
                iface_dict[desc] = output

            else:
                
                list_len = len(iface_dict[desc])
                
                if len(iface_dict[desc]) >= 1:

                    if len(iface_dict[desc]) == 1:
                    
                        difbytes = int(output) - int(iface_dict[desc][0])
                        iface_dict[desc].append(difbytes)
                
                    else:

                        difbytes = int(output) - int(iface_dict[desc][0])
                        difbytes = difbytes - int(iface_dict[desc][-1])
                        iface_dict[desc].append(difbytes)

                else:
                    
                    iface_dict[desc].append(output)

        time.sleep(300)


    for desc in iface_dict:
        
        if 'ifDescr' not in desc:

            iface_dict[desc] = iface_dict[desc][1:]                
    
    #pprint(iface_dict)
    return iface_dict



def octet_chart(in_octets, out_octets, intf_name):

    # Create object of type pygal line chart
    line_chart = pygal.Line()
    
    # Assign title
    line_chart.title = "pynet-rtr1 %s In/Out Bytes" % intf_name

    # X-axis labels
    line_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']

    # Add in/out octets lists to graph with label
    line_chart.add('InBytes', in_octets)
    line_chart.add('OutBytes', out_octets)

    # Create image file from chart
    line_chart.render_to_file('octet_chart.svg')


def packet_chart(in_pkts, out_pkts, intf_name):

    # Create object of type pygal line chart
    line_chart = pygal.Line()

    # Assign title
    line_chart.title = "pynet-rtr1 %s In/Out Packets" % intf_name

    # X-axis labels
    line_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']

    # Add in/out octets lists to graph with label
    line_chart.add('InPkts', in_pkts)
    line_chart.add('OutPkts', out_pkts)

    # Create image file from chart
    line_chart.render_to_file('packet_chart.svg')





if __name__ == '__main__':

    snmp_data = intf_data()
    intf_name = snmp_data['ifDescr_fa4']
    in_bytes = snmp_data['ifInOctects_fa4']
    out_bytes = snmp_data['ifOutOctets_fa4']
    in_pkts = snmp_data['ifInUcastPkts_fa4']
    out_pkts = snmp_data['ifOutUcastPkts_fa4']


    octet_chart(in_bytes, out_bytes, intf_name)
    packet_chart(in_pkts, out_pkts, intf_name)

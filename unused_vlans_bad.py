# Import statements
import os
import sys
import socket
import getpass
core_list = ['be-core-1' , 'brd-core-1' , 'bs-core-1' , 'bw-core-1' , 'cb-core-1' , 'cl-core-1' , 'cl-core-2' , 'eh-core-2' , 'fq-core-2' , 'fr-core-1' , 'gbg-core-1' , 'jhn-core-1' , 'mc-core-1' , 'ps-core-1' , 'rd-core-1' , 'sc-core-1' , 'sc-core-2' , 'th-core' , 'ttv-core-1' , ]
while True:
    core = input("be-core-1\nbrd-core-1\nbs-core-1\nbw-core-1\ncb-core-1\ncl-core-1\ncl-core-2\neh-core-2\nfq-core-2\nfr-core-1\ngbg-core-1\njhn-core-1\nmc-core-1\nps-core-1\nrd-core-1\nsc-core-1\nsc-core-2\nth-core\nttv-core-1\nPlease select the core # you would like to check:")
    if any(item.lower() == core.lower() for item in core_list):
        break
    print ("\n\n\nPlease enter the name exacly as it appears in the list.\n ")


with open('vlan_arp_counts.log', 'r') as infile:
    for line in infile:
        line = line.strip('\n')
        if line.endswith(',2') or line.endswith(',1') or line.endswith('0'):
            line = (line)
            if core in line:
                print (line)
#                if 'Vlan' in line:
#                    print (line)
#            

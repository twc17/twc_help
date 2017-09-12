#!/usr/bin/python3

# Author: Troy W. Caro <twc17@pitt.edu>
# Author 2: Lucci <lucci@pitt.edu>
# Date: Sep 11, 2017 
# Version: 1.0.0
#
# Purpose:
#   This script uses the output file generated from vlan_usage_via_arp_entries.pl
#   It will then output all of the VLANs with 2 or less entries in the ARP table
#
# Useage:
#   python3 ununsed_vlans.py <FILE_OF_ARP_ENTRIES>.txt

# Imports
import os
import sys
import smtplib
core_list = ['be-core-1' , 'brd-core-1' , 'bs-core-1' , 'bw-core-1' , 'cb-core-1' , 'cl-core-1' , 'cl-core-2' , 'eh-core-2' , 'fq-core-2' , 'fr-core-1' , 'gbg-core-1' , 'jhn-core-1' , 'mc-core-1' , 'ps-core-1' , 'rd-core-1' , 'sc-core-1' , 'sc-core-2' , 'th-core' , "ttv-core-1" , ]
while True:
    core = raw_input("be-core-1\nbrd-core-1\nbs-core-1\nbw-core-1\ncb-core-1\ncl-core-1\ncl-core-2\neh-core-2\nfq-core-2\nfr-core-1\ngbg-core-1\njhn-core-1\nmc-core-1\nps-core-1\nrd-core-1\nsc-core-1\nsc-core-2\nth-core\nttv-core-1\nPlease select the core # you would like to check:")
    if any(item.lower() == core.lower() for item in core_list):
        break
    print ("\n\n\nPlease enter the name exacly as it appears in the list.\n ")


arp_file = open('log/vlan_usage_via_arp_entries/VLAN_ARP_COUNTS.log', 'r')
for line in arp_file:
    line = line.split(',')
    if int (line[-1]) <= 2:                                               # This will get the last item of the list
        line = (",".join(line))
        if core in line:
            line = (line)
            if 'Vlan' in line:
                print(line)
#        output = open('unused_vlans.txt', 'w')
#        output.write(",".join(line))
#        output.close()

arp_file.close()                                                    # Don't forget to close the file after reading!

# Time to build the email
#msg = MIMEMultipart()
#msg['Subject'] = "Unused VLANs"
#msg['From'] = "nocjob@tsunami.ns.pitt.edu"
#msg['To'] = "pittnet-techs-l@list.pitt.edu"

# For line in log file
#   split by ','
#   *whatever field number of entries is
#   if number of entries is <=2:
#       write line to output file
# send mail to pitt-techs list

# Thats basically it

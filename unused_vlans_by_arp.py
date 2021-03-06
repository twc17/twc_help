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
arp_file = open('log/vlan_usage_via_arp_entries/VLAN_ARP_COUNTS.log', 'r')
for line in arp_file:
    line = line.split(',')
    if int (line[-1]) <= 2:                                               # This will get the last item of the list
        line = (",".join(line))
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

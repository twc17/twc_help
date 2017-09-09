# Author: Troy W. Caro <twc17@pitt.edu>
# Date: Sep 8, 2017 
# Version: 1.0.0
#
# Purpose:
#   This script uses the output file generated from vlan_usage_via_arp_entries.pl
#   It will then output all of the VLANs with 2 or less entries in the ARP table

# Imports

For line in log file
    split by ','
    *whatever field number of entries is
    if number of entries is <=2:
        write line to output file
send mail to pitt-techs list

# Thats basically it

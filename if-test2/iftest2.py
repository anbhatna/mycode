#!/usr/bin/python3


ipchk =input('Apply an IP address')
try:
    ipaddress.ip_address(ipchk)

    if ipchk:
        print('Looks like the IP address was set: '+ipchk)
    else: #if no data provided

        print ('You have not provided any data')
except:
    print("That doesn't appear to be a valid ipaddress")

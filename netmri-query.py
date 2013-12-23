#!/usr/bin/python
import sys
import json
import requests
import pprint

ADDRESS = '10.240.128.225'
USERNAME = 'rancid'
PASSWORD = 'h4k2dJm6'
PATH = '/api/'
VERIFY = False
VERSION = '2.8'

def make_req():
    r = requests.get('https://' + ADDRESS + PATH + VERSION + '/end_host_mac_addresses/search.json?MACAddress=18:03:73:C9:A8:52&sort=EndHostMACAddressTimestamp', auth=(USERNAME, PASSWORD), verify=VERIFY)
    foo = r.json()
    bar = foo['end_host_mac_addresses'].pop()
    
    print json.dumps(bar, sort_keys=True, indent=4, separators=(',',': '))

#    r = requests.get('https://' + ADDRESS + PATH + VERSION + '/neighbors/device.json?NeighborID=25288631', auth=(USERNAME, PASSWORD), verify=VERIFY)
#    foo = r.json()
#    print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',',': '))

def main():
    make_req()

if __name__ == '__main__':
    sys.exit(main())

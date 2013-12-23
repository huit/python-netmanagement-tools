#!/usr/bin/python
import sys
import json
import requests
import pprint

ADDRESS = '128.103.200.106'
USERNAME = 'api-ro'
PASSWORD = '35LuWKlZnTKbKRbevraK'
PATH = '/wapi/v'
VERIFY = False
VERSION = '1.2'

def make_req():
    r = requests.get('https://' + ADDRESS + PATH + VERSION + '/fixedaddress?ipv4addr~=128.103&_return_fields=ipv4addr,network,mac&_max_results=-10000', auth=(USERNAME, PASSWORD), verify=VERIFY)
    foo = r.json()
    for i in foo:
        print i

def main():
    make_req()

if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/python
import sys
import json
import requests
import pprint
import ConfigParser

class NetMRIConn:
    def __init__(self, conffile):
        config = ConfigParser.ConfigParser()
        try:
            config.read(conffile)
        except:
            print "failed opening config file, giving up"
            sys.exit(0)
        try:
            self.address = config.get('NetMRI', 'address')
            self.username = config.get('NetMRI', 'username')
            self.path = config.get('NetMRI', 'path')
            self.password = config.get('NetMRI', 'password')
            self.version = config.get('NetMRI', 'version')
            if config.get('NetMRI', 'verify') == 'True':
                self.verify = True
            else:
                self.verify = False
        except:
            print "conf file appears to be corrupt or does not contain all needed values to set up NetMRI connection"
            sys.exit(0)

    def getlastseenbymac(self, macaddr):

        # gets the most recent time seen from netmri for a given mac address
        # returns none if mac address is not seen

        r = requests.get('https://' + self.address + self.path + self.version + '/end_host_mac_addresses/search.json?MACAddress=' + macaddr + '&sort=EndHostMACAddressTimestamp', auth=(self.username, self.password), verify=self.verify)
        foo = r.json()
        if foo['current'] != 0:
            return foo['end_host_mac_addresses'].pop()
        else:
            return None



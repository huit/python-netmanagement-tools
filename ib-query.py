#!/usr/bin/python
import sys
import json
import requests
import pprint
import ConfigParser

class InfobloxConn:
    def __init__(self, conffile):
        config = ConfigParser.ConfigParser()
        try:
            config.read(conffile)
        except:
            print "failed opening config file, giving up"
            sys.exit(0)
        try:
            self.ib_address = config.get('IB', 'address')
            self.username = config.get('IB', 'username')
            self.path = config.get('IB', 'path')
            self.password = config.get('IB', 'password')
            self.version = config.get('IB', 'version')
            if config.get('IB', 'verify') == 'True':
                self.verify = True
            else:
                self.verify = False
        except:
            print "conf file appears to be corrupt or does not contain all needed values to set up IB connection"
            sys.exit(0)

    def getfixedaddr(self, addr, fields, numresults):
        r = requests.get('https://' + self.ib_address + self.path + self.version + '/fixedaddress?ipv4addr~=' + addr + '&_return_fields=' + fields + '&_max_results=-' + str(numresults), auth=(self.username, self.password), verify=self.verify)
        return r.json()

def main():
    a = InfobloxConn('ib.cfg')
    r = a.getfixedaddr('128.103.209', 'ipv4addr,network,mac', 10000)
    for i in r:
        print i

if __name__ == '__main__':
    sys.exit(main())

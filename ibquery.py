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

    def getfixedaddr(self, ipaddr, fields, numresults):

        # gets all fixed addresses in a given network range

        r = requests.get('https://' + self.ib_address + self.path + self.version + '/fixedaddress?ipv4addr~=' + ipaddr + '&_return_fields=' + fields + '&_max_results=-' + str(numresults), auth=(self.username, self.password), verify=self.verify)
        return r.json()

    def getmacfilteraddress(self, macaddr, fields, numresults):

        r = requests.get('https://' + self.ib_address + self.path + self.version + '/macfilteraddress?mac=' + macaddr + '&_return_fields=' + fields + '&_max_results=-' + str(numresults), auth=(self.username, self.password), verify=self.verify)
        return r.json()

    def getleasebyip(self, ipaddr, fields, numresults):

        r = requests.get('https://' + self.ib_address + self.path + self.version + '/lease?address=' + ipaddr + '&_return_fields=' + fields + '&_max_results=-' + str(numresults), auth=(self.username, self.password), verify=self.verify)
        return r.json()

    def getauthzone(self, zonename, fields):

        r = requests.get('https://' + self.ib_address + self.path + self.version + '/zone_auth?fqdn=' + zonename + '&_return_fields=' + fields, auth=(self.username, self.password), verify=self.verify)
        return r.json()

    def getdelegatedzone(self, zonename, fields):

        r = requests.get('https://' + self.ib_address + self.path + self.version + '/zone_delegated?fqdn=' + zonename + '&_return_fields=' + fields, auth=(self.username, self.password), verify=self.verify)
        return r.json()

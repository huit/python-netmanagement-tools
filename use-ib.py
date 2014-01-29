#!/usr/bin/python
import sys
import ibquery
import netmriquery

def main():
    ib = ibquery.InfobloxConn('ib.cfg')
    netmri = netmriquery.NetMRIConn('netmri.cfg')

    r = ib.getfixedaddr('10.243.37', 'ipv4addr,network,mac', 10000)
    print 'mac addr , fixed ip , last seen date , last seen ip, mac last seen at fixed ip'
    for i in r:
        lastseenbymac = netmri.getlastseenbymac(i['mac'])
        lastseenbyip = netmri.getlastseenbyip(i['ipv4addr'])
        print i['mac'] + "," + i['ipv4addr'] + ",",
        if lastseenbymac != None:
            print lastseenbymac['EndHostMACAddressStartTime'] + "," + lastseenbymac['IPAddress'] + ",",
        else:
            print ',,',
        if lastseenbyip != None:
            print lastseenbyip['MACAddress']
        else:
            print ''

if __name__ == '__main__':
    sys.exit(main())

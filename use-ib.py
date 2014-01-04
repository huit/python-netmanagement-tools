#!/usr/bin/python
import sys
import ibquery
import netmriquery

def main():
    ib = ibquery.InfobloxConn('ib.cfg')
    netmri = netmriquery.NetMRIConn('netmri.cfg')

    r = ib.getfixedaddr('128.103.209', 'ipv4addr,network,mac', 10000)
    print 'fixed addresses in this range:'
    print
    print 'mac addr , fixed ip , last seen date , last seen ip'
    for i in r:
        lastseen = netmri.getlastseenbymac(i['mac'])
        print i['mac'] + "," + i['ipv4addr'] + ",",
        if lastseen != None:
            print lastseen['EndHostMACAddressStartTime'] + "," + lastseen['IPAddress']
        else:
            print 'none'

    print
    


if __name__ == '__main__':
    sys.exit(main())

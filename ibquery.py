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

        if self.version == '1.2':
            self.ib_fixedaddr_fields = 'agent_circuit_id,agent_remote_id,always_update_dns,bootfile,bootserver,client_identifier_prepend_zero,comment,ddns_domainname,ddns_hostname,deny_bootp,dhcp_client_identifier,disable,discovered_data,enable_ddns,extattrs,ignore_dhcp_option_list_request,ipv4addr,mac,match_client,ms_options,ms_server,name,network,network_view,nextserver,options,pxe_lease_time,use_bootfile,use_bootserver,use_ddns_domainname,use_deny_bootp,use_enable_ddns,use_ignore_dhcp_option_list_request,use_nextserver,use_options'
            self.ib_lease_fields = 'address,billing_class,binding_state,client_hostname,cltt,discovered_data,ends,hardware,ipv6_duid,ipv6_iaid,ipv6_preferred_lifetime,ipv6_prefix_bits,network,network_view,never_ends,never_starts,next_binding_state,on_commit,on_expiry,on_release,option,protocol,served_by,server_host_name,starts,tsfp,tstp,uid,username,variable'
            self.ib_macfilteraddress_fields = 'authentication_time,comment,expiration_time,extattrs,filter,guest_custom_field1,guest_custom_field2,guest_custom_field3,guest_custom_field4,guest_email,guest_first_name,guest_last_name,guest_middle_name,guest_phone,is_registered_user,mac,never_expires,reserved_for_infoblox,username'
            self.ib_zone_auth_fields = 'address,allow_active_dir,allow_gss_tsig_for_underscore_zone,allow_gss_tsig_zone_updates,allow_query,allow_transfer,allow_update,allow_update_forwarding,comment,copy_xfer_to_notify,create_underscore_zones,disable,disable_forwarding,display_domain,dns_fqdn,dns_soa_email,dns_soa_mname,dnssec_key_params,effective_check_names_policy,effective_record_name_policy,extattrs,external_primaries,external_secondaries,fqdn,grid_primary,grid_primary_shared_with_ms_parent_delegation,grid_secondaries,is_dnssec_enabled,is_dnssec_signed,last_queried,locked,locked_by,mask_prefix,ms_ad_integrated,ms_allow_transfer,ms_allow_transfer_mode,ms_ddns_mode,ms_managed,ms_primaries,ms_read_only,ms_secondaries,ms_sync_master_name,network_associations,network_view,notify_delay,ns_group,parent,prefix,primary_type,record_name_policy,records_monitored,rr_not_queried_enabled_time,soa_default_ttl,soa_email,soa_expire,soa_mname,soa_negative_ttl,soa_refresh,soa_retry,soa_serial_number,srgs,update_forwarding,use_allow_active_dir,use_allow_transfer,use_allow_update,use_allow_update_forwarding,use_check_names_policy,use_copy_xfer_to_notify,use_dnssec_key_params,use_external_primary,use_grid_zone_timer,use_import_from,use_record_name_policy,use_soa_email,use_soa_mname,using_srg_associations,view,zone_format,zone_not_queried_enabled_time'
            self.ib_zone_delegated_fields = 'address,comment,delegate_to,delegated_ttl,disable,display_domain,dns_fqdn,enable_rfc2317_exclusion,extattrs,fqdn,locked,locked_by,mask_prefix,ms_ad_integrated,ms_ddns_mode,ms_managed,ms_read_only,ms_sync_master_name,parent,prefix,use_delegated_ttl,using_srg_associations,view,zone_format'

    def get_fixedaddress (self, keyfield, key, numresults):

        r = requests.get('https://' + self.ib_address + self.path + self.version + '/fixedaddress?' + keyfield + '=' + key + '&_return_fields=' + self.ib_fixedaddr_fields + '&_max_results=-' + str(numresults), auth=(self.username, self.password), verify=self.verify)
        return r.json()

    def get_lease (self, keyfield, key, numresults):

        r = requests.get('https://' + self.ib_address + self.path + self.version + '/lease?' + keyfield + '=' + key + '&_return_fields=' + self.ib_lease_fields + '&_max_results=-' + str(numresults), auth=(self.username, self.password), verify=self.verify)
        return r.json()

    def get_macfilteraddress (self, keyfield, key, numresults):

        r = requests.get('https://' + self.ib_address + self.path + self.version + '/macfilteraddress?' + keyfield + '=' + key + '&_return_fields=' + self.ib_macfilteraddress_fields + '&_max_results=-' + str(numresults), auth=(self.username, self.password), verify=self.verify)
        return r.json()

    def get_zone_auth (self, keyfield, key):

        r = requests.get('https://' + self.ib_address + self.path + self.version + '/zone_auth?' + keyfield + '=' + key + '&_return_fields=' + self.ib_zone_auth_fields, auth=(self.username, self.password), verify=self.verify)
        return r.json()

    def get_zone_delegated (self, keyfield, key):

        r = requests.get('https://' + self.ib_address + self.path + self.version + '/zone_delegated?' + keyfield + '=' + key + '&_return_fields=' + self.ib_zone_delegated_fields, auth=(self.username, self.password), verify=self.verify)
        return r.json()


#!/usr/bin/python3

import logging
import requests

def get_platform(platform):
    if platform == 'IOS-XE':
        device_sufix_name = '-CSR1kv'
        ned = '<ned-id xmlns:cisco-ios-cli-6.42="http://tail-f.com/ns/ned-id/cisco-ios-cli-6.42">cisco-ios-cli-6.42:cisco-ios-cli-6.42</ned-id>'
    elif platform == 'IOS-XR':
        device_sufix_name = '-ASR9kv'
        ned = '<ned-id xmlns:cisco-iosxr-cli-7.18="http://tail-f.com/ns/ned-id/cisco-iosxr-cli-7.18">cisco-iosxr-cli-7.18:cisco-iosxr-cli-7.18</ned-id>'
    logging.debug(f'!!! NSO_ZTP_SCRIPT: Platform Set: {device_sufix_name}')
    return device_sufix_name, ned

def add_device(nso_socket, hostname, ipaddr, platform):
    logging.debug(f'!!! NSO_ZTP_SCRIPT: Started.')
    device_sufix_name, ned = get_platform(platform)

    url = 'http://' + nso_socket + '/restconf/data/tailf-ncs:devices'

    header = {
        'Authorization': 'Basic YWRtaW46YWRtaW4=',
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+xml'
    }

    payload = (
        '<device>\n'
        '   <name>' + hostname + '</name>\n'
        '   <address>' + ipaddr + '</address>\n'
        '   <description>ZTP' + device_sufix_name + '</description>\n'
        '   <authgroup>ztp_authgrp</authgroup>\n'
        '   <device-type>\n'
        '   <cli>\n' + ned + '\n'
        '   </cli>\n'
        '   </device-type>\n'
        '   <state>\n'
        '   <admin-state>unlocked</admin-state>\n'
        '   </state>\n'
        '</device>\n'
    )

    response = requests.post(url, headers=header, data=payload)
    logging.debug(f'!!! NSO_ZTP_SCRIPT: Device Added... RESTCONF Response Code: {response.status_code}')
    return response.status_code

def device_ssh_keys(nso_socket, hostname):

    url = 'http://' + nso_socket + '/restconf/data/tailf-ncs:devices/device=' + hostname + '/ssh/fetch-host-keys'

    header = {
        'Authorization': 'Basic YWRtaW46YWRtaW4=',
        'Accept': 'application/yang-data+json',
    }

    response = requests.post(url, headers=header)
    logging.debug(f'!!! NSO_ZTP_SCRIPT: SSH Keys Fetched... RESTCONF Response Code: {response.status_code}')
    return response.status_code

def device_sync_from(nso_socket, hostname):

    url = 'http://' + nso_socket + '/restconf/data/tailf-ncs:devices/device=' + hostname + '/sync-from'

    header = {
        'Authorization': 'Basic YWRtaW46YWRtaW4=',
        'Accept': 'application/yang-data+json',
    }

    response = requests.post(url, headers=header)
    logging.debug(f'!!! NSO_ZTP_SCRIPT: Device Synced...RESTCONF Response Code: {response.status_code}')
    return response.status_code

def create_golden_config_service(nso_socket, service_name, platform, hostname, ipaddr, region):

    url = 'http://' + nso_socket + '/restconf/data/tailf-ncs:services/nso_golden_config:nso_golden_config/'

    header = {
        'Authorization': 'Basic YWRtaW46YWRtaW4=',
        'Accept': 'application/yang-data+json',
        'Content-Type': 'application/yang-data+xml'
    }

    payload = (
        '<nso_golden_config xmlns=\"http://example.com/nso_golden_config\">\n'
        '    <service_instance>' + service_name + '</service_instance>\n'
        '    <platform>' + platform + '</platform>\n'
        '    <device>' + hostname + '</device>\n'
        '    <hostname>' + hostname + '</hostname>\n'
        '    <mgmt_ip_addr>' + ipaddr + '</mgmt_ip_addr>\n'
        '    <Region>' + region + '</Region>\n'
        '</nso_golden_config>'
    )

    response = requests.patch(url, headers=header, data=payload)
    logging.debug(f'!!! NSO_ZTP_SCRIPT: GOLDEN CONFIG SERVICE... RESTCONF Response Code: {response.status_code}')
    return response.status_code
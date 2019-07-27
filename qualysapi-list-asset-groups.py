#!/usr/bin/env python3

# Use the defusedxml package for all xml parsing. See bandit docs: 
# https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b405-import-xml-etree
from defusedxml.ElementTree import fromstring
from qualysapi import connect

# Config settings
delimiter = "|"
api_url = "/api/2.0/fo/asset/group"
out_file = "out-asset-groups-list.csv"

# Connect to Qualys API
conn = connect()

# Options for API request. See qualys docs for a list of all options
params = {'action': 'list',
          'truncation_limit': '0'}

# Perform API request
resp = conn.request(api_url, params)

# Parse the response string and convert to an xml object
xml = fromstring(resp.encode('utf-8'))
ags = {}
with open(out_file, "w+") as f:
    f.write('id' + delimiter + 'title' + delimiter + 'network_id' + delimiter + \
            'ip_ranges' + '\n')
    for ag in xml.iter(tag='ASSET_GROUP'):

        # Get the ID for the asset group
        id = ag.find('ID').text

        # Get the title for the asset group
        title = ag.find('TITLE').text

        # Get the Network ID for asset group
        network_id_xml = ag.find('NETWORK_ID')
        if network_id_xml is not None:
            network_id = network_id_xml.text
        else:
            network_id = ""

        # Get the IP ranges in the asset group
        ip_set = ag.find('IP_SET')
        if ip_set:
            ip_ranges = ""
            for ip_range in ip_set.iter(tag='IP_RANGE'):
                ip_ranges += ip_range.text + "; "
            for ip in ip_set.iter(tag='IP'):
                ip_ranges += ip.text + "; "
        else:
            ip_ranges = ""
        
        # write asset group to file
        f.write(id + delimiter + title + delimiter + network_id + delimiter + \
                ip_ranges + "\n")


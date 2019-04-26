#!/usr/bin/python

from requests import get

ipv4 = get('https://api.ipify.org').text
print('My public IPv4 address is: {}'.format(ipv4))
ipv6 = get('https://api6.ipify.org').text
print('My public IPv6 address is: {}'.format(ipv6))

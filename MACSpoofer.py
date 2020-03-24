#!/usr/bin/env python

import subprocess
import optparse
import re

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, user --help for more info")
    if not options.new_mac:
        parser.error("[-] Please specify a new MAC address, user --help for more info")
    return options

def get_current_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")

def spoof_mac_address(interface, new_mac_address):
    print("[+] Changing MAC address for " + interface + " to " + new_mac_address)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
    subprocess.call(["ifconfig", interface, "up"])

options = get_args()

current_mac_address = get_current_mac_address(options.interface)
print("Current MAC = " + str(current_mac_address))

spoof_mac_address(options.interface, options.new_mac)

current_mac_address = get_current_mac_address(options.interface)

if current_mac_address == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac_address)
else:
    print("[-] MAC address did not get changed.")



#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, user --help for more info")
    if not options.new_mac:
        parser.error("[-] Please specify a new MAC address, user --help for more info")
    return options


def spoof_mac(interface, new_mac_address):
    print("[+] Changing MAC address for " + interface + " to " + new_mac_address)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
spoof_mac(options.interface, options.new_mac)

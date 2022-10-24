import subprocess
import optparse

def takeArgs():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface_name", help="Name of the interface whose mac you want to change")
    parser.add_option("-m", "--mac", dest="new_mac_address", help="New mac address that you want to assign")
    (opt, args) = parser.parse_args()
    if(opt.interface_name==None or opt.interface_name==""):
        if (opt.new_mac_address == None or opt.new_mac_address == ""):
            parser.error("[-] Please specify interface and mac address, use --help for more info.")
        else:
            parser.error("[-] Please specify an interface, use --help for more info.")
    else:
        if (opt.new_mac_address == None or opt.new_mac_address == ""):
            parser.error("[-] Please specify a mac address, use --help for more info.")
        else:
            return opt

def changeMac(interface_name, new_mac):
    print("\n[+] changing mac of " + interface_name + " to " + new_mac)
    subprocess.call(["ifconfig", interface_name, "down"])
    subprocess.call(["ifconfig", interface_name, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface_name, "up"])
    print("[+] changed mac of " + interface_name)

#body starts here

options = takeArgs()
changeMac(options.interface_name, options.new_mac_address)

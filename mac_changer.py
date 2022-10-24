import subprocess

subprocess.call("ifconfig",shell=True)
interface_name = input("\n\n\n>> Enter interface name :- ")
new_mac = input(">>Enter new macaddress :- ")

#this is not a secure way to write code it can easily be corupted using shell code injection
#subprocess.call("ifconfig "+interface_name+" down",shell=True)
#subprocess.call("ifconfig "+interface_name+" hw ether "+new_mac,shell=True)
#subprocess.call("ifconfig "+interface_name+" up",shell=True)
print("\n[+] changing mac of "+interface_name+" to "+new_mac)
subprocess.call(["ifconfig", interface_name, "down"])
subprocess.call(["ifconfig", interface_name, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface_name, "up"])
print("[+] changed mac of "+interface_name)
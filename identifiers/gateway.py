import netifaces
import ipaddress
import requests
import subprocess
from scapy.all import ARP, Ether, srp

<<<<<<< HEAD


def gateway_info():
    #Gateway Variables
    gws = netifaces.gateways()
    router_ip, iface = gws["default"][netifaces.AF_INET]
    ip_info = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]
    addr  = ip_info["addr"]
    mask = ip_info["netmask"]
    subnet = ipaddress.IPv4Network(f"{addr}/{mask}", strict = False)
    
    try:
        info = {"Gateway": router_ip,"Interface": iface, "Subnet": subnet}
=======
def gateway_info():
    try:
        gws = netifaces.gateways()
        router_ip, iface = gws["default"][netifaces.AF_INET]
        ip_info = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]
        info = {"Gateway": router_ip,"Interface": ip_info}
    
        
        return info
>>>>>>> 15bbdbd (first successful version)

    except Exception as e:
        print(f"[!]Error! {e}. Please try again. [!]")
        return None




def get_gateway_mac():

    gw = gateway_info()
    gateway_ip = gw.get("Gateway")

    arp = ARP(pdst=gateway_ip)
    ether = Ether(dst = "ff:ff:ff:ff:ff:ff")

    pkt = ether/arp

    try:
        answered, _ = srp(pkt, timeout = 0, verbose =0)
    except Exception as e:
        print(f"error. {e}")
        return None

    for sent, received in answered:
        return received.hwsrc

